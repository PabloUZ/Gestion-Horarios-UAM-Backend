from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.api.config.database import Base

class Faculty(Base):
    __tablename__ = "faculties"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=50), nullable=False)
    programs = relationship("Program", back_populates="faculty")