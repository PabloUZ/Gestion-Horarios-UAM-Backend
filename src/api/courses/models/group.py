from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import relationship 
from src.api.config.database import Base

class Group(Base):    
    __tablename__ = "groups"    

    id                = Column(Integer, primary_key=True, autoincrement=True)      
    name                = Column(String(length=60))

    professor = relationship("Professor", back_populates="group")
    classtime = relationship("Classtime", back_populates="group")
    course = relationship("Course", back_populates="group")