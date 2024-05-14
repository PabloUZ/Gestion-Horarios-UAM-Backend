from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.api.config.database import Base


class Course(Base):
    __tablename__ = "courses"

    code                = Column(Integer, primary_key=True, autoincrement=True)      
    name                = Column(String(length=60))
    credits             = Column(Integer)
    type                = Column(String(length=60))

    group = relationship("Group", back_populates="course")
    courses_approved = relationship("CourseApproved", back_populates="course")
    courses_offered = relationship("CourseOffered", back_populates="course")