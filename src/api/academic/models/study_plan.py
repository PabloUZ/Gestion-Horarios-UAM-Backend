from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.api.config.database import Base

class StudyPlan(Base):
    __tablename__ = "study_plan"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=50), nullable=False)
    year = Column(Integer, nullable=False)
    program_id = Column(Integer, ForeignKey("program.id"), nullable=True)
    
    program = relationship("Program", back_populates="study_plan")