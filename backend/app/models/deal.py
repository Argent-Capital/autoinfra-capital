from sqlalchemy import Column, Integer, String, Float
from ..db.base import Base

class Deal(Base):
    __tablename__ = "deals"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    sector = Column(String, nullable=False)
    country = Column(String, nullable=False)
    capex = Column(Float, nullable=False)
    irr_estimate = Column(Float, default=0.0)
    esg_score = Column(Float, default=0.0)
    carbon_yield = Column(Float, default=0.0)
    status = Column(String, default="screening")
