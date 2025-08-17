# Data Model (simplified)

- Investor(id, name, email, status, kyc_level, wallet_address)
- Deal(id, title, sector, country, capex, irr_estimate, esg_score, carbon_yield, status)
- Investment(id, investor_id, deal_id, amount, date)
- Report(id, period, url, hash)

Postgres with SQLAlchemy models in `backend/app/models`.
