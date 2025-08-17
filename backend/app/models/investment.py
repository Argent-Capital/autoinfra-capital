from sqlalchemy import Column, Integer, ForeignKey, Float, Date
from ..db.base import Base

class Investment(Base):
    __tablename__ = "investments"
    id = Column(Integer, primary_key=True, index=True)
    investor_id = Column(Integer, ForeignKey("investors.id"))
    deal_id = Column(Integer, ForeignKey("deals.id"))
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
