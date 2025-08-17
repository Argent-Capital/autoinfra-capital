# API (v1)

## Health
GET `/health`

## Investors
- POST `/v1/investors` create
- GET `/v1/investors/{id}`
- POST `/v1/investors/{id}/kyc` (mock)
- GET `/v1/investors` list

## Deals
- POST `/v1/deals/score` → returns score + memo id
- GET `/v1/deals/{id}`
- GET `/v1/deals`

## Reports
- POST `/v1/reports/quarterly` (generate)
- GET `/v1/reports/{id}`
