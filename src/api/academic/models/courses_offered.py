from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.api.config.database import Base

class CourseOffered(Base):
    __tablename__ = "course_offered"
    
    course_id = Column(Integer, ForeignKey("course.id"), primary_key=True)
    study_plan_id = Column(Integer, ForeignKey("study_plan.id"), primary_key=True)
    
    course = relationship("Course", back_populates="courses_offered")
    study_plan = relationship("StudyPlan", back_populates="courses_offered")