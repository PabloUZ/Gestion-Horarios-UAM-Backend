from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.api.config.database import Base

class CourseApproved(Base):
    __tablename__ = "course_approved"
    
    course_id = Column(Integer, ForeignKey("course.id"), primary_key=True)
    academic_history_id = Column(Integer, ForeignKey("academic_history.id"), primary_key=True)
    
    course = relationship("Course", back_populates="courses_approved")
    academic_history = relationship("AcademicHistory", back_populates="courses_approved")