from pydantic import BaseModel, Field

class DealScoreRequest(BaseModel):
    title: str
    sector: str
    country: str
    capex: float
    cashflows: list[float] = Field(..., description="Year 0..N cashflows (include negative capex)")
    esg_inputs: dict = {}

class DealScoreResponse(BaseModel):
    irr: float
    npv_10: float
    esg_score: float
    carbon_yield: float
    total_score: float
    memo: str
