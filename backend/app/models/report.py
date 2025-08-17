from sqlalchemy import Column, Integer, String
from ..db.base import Base

class Report(Base):
    __tablename__ = "reports"
    id = Column(Integer, primary_key=True, index=True)
    period = Column(String, nullable=False)  # e.g., "2025-Q3"
    url = Column(String, nullable=False)
    hash = Column(String, nullable=False)
