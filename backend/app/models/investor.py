from sqlalchemy import Column, Integer, String
from ..db.base import Base

class Investor(Base):
    __tablename__ = "investors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    status = Column(String, default="pending")
    kyc_level = Column(String, default="none")
    wallet_address = Column(String, nullable=True)
