def esg_score(inputs: dict) -> float:
    # Very simple placeholder: weighted sum
    env = inputs.get("environment", 0)
    social = inputs.get("social", 0)
    governance = inputs.get("governance", 0)
    return 0.5*env + 0.3*social + 0.2*governance
