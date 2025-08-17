def estimate_carbon_yield(sector: str, capex: float) -> float:
    # Simplified model: energy projects yield higher credits per capex
    base = 0.0
    if sector.lower() in {"energy", "solar", "wind"}:
        base = 0.12
    elif sector.lower() in {"water"}:
        base = 0.07
    elif sector.lower() in {"transport"}:
        base = 0.05
    else:
        base = 0.03
    return base * (capex / 1_000_000)  # credits per R1m capex (placeholder)
