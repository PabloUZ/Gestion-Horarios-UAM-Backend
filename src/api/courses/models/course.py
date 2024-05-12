from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.api.config.database import Base


class Course(Base):
    __tablename__ = "courses"

    code = Column(String(length=4), primary_key=True)
    name = Column(String(length=60))
    credits = Column(Integer)
    type_id = Column(Integer, ForeignKey('course_types.id'))

    groups = relationship("Group", back_populates="course")
    course_type = relationship("CourseType", back_populates="courses")
