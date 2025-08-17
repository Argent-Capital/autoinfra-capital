# Architecture

```text
[Frontend (React)] <-> [FastAPI Backend] <-> [Postgres]
         |                    |                 |
         v                    v                 v
   Investor UI        Deal Engine / API     Persistent store
         |
         v
[Automation Pipelines] -- scraping, scoring, reports
         |
         v
[Contracts (Solidity)] -- subscriptions & distributions
```

Key services:
- **Deal Engine:** scoring, ESG, carbon credit yield
- **KYC/Compliance (stub):** pluggable verification
- **Reporting:** quarterly PDF (templated) + dashboard KPIs
- **Orchestration:** cron/Cloud scheduler or GitHub Actions

See `processes.md` for flows.
