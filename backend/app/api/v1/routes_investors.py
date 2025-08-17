from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...db.session import SessionLocal, engine
from ...db.base import Base
from ...models.investor import Investor
from ...schemas.investor import InvestorCreate, InvestorOut
from ...services.kyc import verify_kyc

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create tables on import (simple demo)
Base.metadata.create_all(bind=engine)

@router.post("", response_model=InvestorOut)
def create_investor(payload: InvestorCreate, db: Session = Depends(get_db)):
    existing = db.query(Investor).filter(Investor.email == payload.email).first()
    if existing:
        raise HTTPException(status_code=409, detail="Investor already exists")
    inv = Investor(name=payload.name, email=payload.email, wallet_address=payload.wallet_address or None)
    db.add(inv)
    db.commit()
    db.refresh(inv)
    return inv

@router.get("/{investor_id}", response_model=InvestorOut)
def get_investor(investor_id: int, db: Session = Depends(get_db)):
    inv = db.query(Investor).get(investor_id)
    if not inv:
        raise HTTPException(status_code=404, detail="Not found")
    return inv

@router.post("/{investor_id}/kyc", response_model=InvestorOut)
def kyc_investor(investor_id: int, document_hash: str, db: Session = Depends(get_db)):
    inv = db.query(Investor).get(investor_id)
    if not inv:
        raise HTTPException(status_code=404, detail="Not found")
    status = verify_kyc(document_hash)
    inv.kyc_level = status
    inv.status = "active" if status == "verified" else "pending"
    db.add(inv)
    db.commit()
    db.refresh(inv)
    return inv

@router.get("", response_model=list[InvestorOut])
def list_investors(db: Session = Depends(get_db)):
    return db.query(Investor).limit(100).all()
