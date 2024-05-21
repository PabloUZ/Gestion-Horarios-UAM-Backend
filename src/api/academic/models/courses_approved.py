from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.api.config.database import Base

class CourseApproved(Base):
    __tablename__ = "courses_approved"
    id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(String(length=8), ForeignKey("courses.code"), nullable=False)
    academic_history_id = Column(Integer, ForeignKey("academics_history.id"), nullable=False)
    
    course = relationship("Course", back_populates="courses_approved")
    academic_history = relationship("AcademicHistory", back_populates="courses_approved")