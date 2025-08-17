from fastapi import APIRouter
from ...services.financials import npv
from ...services.memo import build_investment_memo

router = APIRouter()

@router.post("/quarterly")
def generate_quarterly_stub():
    # Placeholder: In production, compile KPIs + PDF
    return {"status":"queued","report_id":"2025-Q3-stub"}
