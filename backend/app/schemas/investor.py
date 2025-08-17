from pydantic import BaseModel, EmailStr

class InvestorCreate(BaseModel):
    name: str
    email: EmailStr
    wallet_address: str | None = None

class InvestorOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    status: str
    kyc_level: str
    wallet_address: str | None
    class Config:
        from_attributes = True
