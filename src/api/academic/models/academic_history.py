from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.api.config.database import Base

class AcademicHistory(Base):
    __tablename__ = "academic_history"

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(String(length=100), nullable=False)
    study_plan_id = Column(Integer, ForeignKey("study_plan.id"), nullable=False)
    
    study_plans = relationship("StudyPlan", back_populates="academic_history")