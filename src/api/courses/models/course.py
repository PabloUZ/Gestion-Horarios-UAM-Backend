from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.api.config.database import Base


class Course(Base):
    __tablename__ = "courses"

    code = Column(String(length=8), primary_key=True)
    name = Column(String(length=100))
    credits = Column(Integer, nullable=True)
    type_id = Column(Integer, ForeignKey('course_types.id'), nullable=True)

    groups = relationship("Group", back_populates="course")
    course_type = relationship("CourseType", back_populates="courses")
    courses_approved = relationship("CourseApproved", back_populates="course")
    courses_offered = relationship("CourseOffered", back_populates="course")
