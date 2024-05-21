from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.api.config.database import Base

class AcademicHistory(Base):
    __tablename__ = "academics_history"

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(String(length=100), nullable=False)
    study_plan_id = Column(Integer, ForeignKey("study_plans.id"), nullable=False)
    user_cc = Column(String(length=10), ForeignKey("users.cc"), nullable=False)
    
    study_plans = relationship("StudyPlan", back_populates="academic_history")
    courses_approved = relationship("CourseApproved", back_populates="academic_history")
    user = relationship("User", back_populates="academic_history")