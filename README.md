# AutoInfra Capital

AI-native, fully automated infrastructure investment platform — from deal sourcing and due diligence to portfolio monitoring and investor reporting.

## ✨ Highlights
- **AI Deal Engine:** automated sourcing, scoring, memos
- **Financial Models:** DCF, IRR, NPV, carbon credit yield
- **Smart Contracts:** investor subscriptions & distributions
- **APIs:** FastAPI backend with typed schemas
- **Dashboard:** React front-end (investor portal)
- **Automations:** scraping pipelines + quarterly reporting
- **Docker:** one-command local dev

> This repository is a **working scaffold**. You can clone and extend to production.

---

## 🚀 Quickstart

### 1) Clone
```bash
git clone https://github.com/<your-org>/autoinfra-capital.git
cd autoinfra-capital
```

### 2) Environment
Copy and edit env:
```bash
cp .env.example .env
```

### 3) Docker (recommended)
```bash
docker compose up --build
```
- Backend: http://localhost:8000/docs
- Frontend: http://localhost:5173

### 4) Dev without Docker
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
uvicorn backend.app.main:app --reload
```

---

## 🧱 Architecture
- `backend/` FastAPI + SQLAlchemy + Pydantic
- `frontend/` React app (Vite)
- `contracts/` Solidity smart contracts
- `automation/` Headless jobs (deal sourcing & reporting)
- `docs/` Process flows, API, data model
- `data/samples/` Seed data for demos

See `docs/architecture.md` and `docs/processes.md` for diagrams and flows.

---

## 🧪 Tests
```bash
pytest backend/app/tests -q
```

## 🔐 Secrets
- Place API keys in `.env` (never commit them).
- OpenAI-style keys are referenced but **not required** to run the stack.

## 🪙 License
MIT
