from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.config import settings
from .api.v1.routes_investors import router as investors_router
from .api.v1.routes_deals import router as deals_router
from .api.v1.routes_reports import router as reports_router

app = FastAPI(title="AutoInfra Capital API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(investors_router, prefix="/v1/investors", tags=["investors"])
app.include_router(deals_router, prefix="/v1/deals", tags=["deals"])
app.include_router(reports_router, prefix="/v1/reports", tags=["reports"])
