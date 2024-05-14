from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.api.config.database import Base

class StudyPlan(Base):
    __tablename__ = "study_plans"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=50), nullable=False)
    year = Column(Integer, nullable=False)
    program_id = Column(Integer, ForeignKey("programs.id"), nullable=True)
    
    academic_history = relationship("AcademicHistory", back_populates="study_plans")
    programs = relationship("Program", back_populates="study_plan")
    courses_offered = relationship("CourseOffered", back_populates="study_plan")