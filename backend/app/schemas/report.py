from pydantic import BaseModel

class ReportOut(BaseModel):
    id: int
    period: str
    url: str
    hash: str
    class Config:
        from_attributes = True
