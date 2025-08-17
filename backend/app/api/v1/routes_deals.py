from fastapi import APIRouter
from ...services.financials import irr, npv
from ...services.esg import esg_score
from ...services.carbon import estimate_carbon_yield
from ...services.memo import build_investment_memo
from ...schemas.deal import DealScoreRequest, DealScoreResponse

router = APIRouter()

@router.post("/score", response_model=DealScoreResponse)
def score_deal(payload: DealScoreRequest):
    # Financials
    irr_val = irr(payload.cashflows)
    npv10_val = npv(0.10, payload.cashflows)
    # ESG & carbon
    esg_val = esg_score(payload.esg_inputs or {})
    carbon_val = estimate_carbon_yield(payload.sector, payload.capex)
    # Total score heuristic
    total = (max(0.0, min(1.0, irr_val/0.25)) * 0.5) + (esg_val/100 * 0.3) + (min(1.0, carbon_val/10) * 0.2)
    memo = build_investment_memo(payload.model_dump(), irr_val, npv10_val, esg_val, carbon_val)
    return DealScoreResponse(
        irr=irr_val, npv_10=npv10_val, esg_score=esg_val,
        carbon_yield=carbon_val, total_score=total, memo=memo
    )
