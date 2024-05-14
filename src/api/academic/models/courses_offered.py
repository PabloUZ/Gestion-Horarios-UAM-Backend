from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.api.config.database import Base

class CourseOffered(Base):
    __tablename__ = "courses_offered"
    id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(String(length=8), ForeignKey("courses.code"))
    study_plan_id = Column(Integer, ForeignKey("study_plans.id"))
    
    course = relationship("Course", back_populates="courses_offered")
    study_plan = relationship("StudyPlan", back_populates="courses_offered")