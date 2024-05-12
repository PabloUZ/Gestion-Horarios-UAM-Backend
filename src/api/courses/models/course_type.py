from sqlalchemy import Boolean, Column, Integer, String 
from sqlalchemy.orm import relationship 
from src.api.config.database import Base

class CourseType(Base):    
    __tablename__ = "course_types"    

    id              = Column(Integer, primary_key=True, autoincrement=True)      
    name            = Column(String(length=60))

    courses = relationship("Course", back_populates="course_type")