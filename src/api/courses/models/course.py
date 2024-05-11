from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import relationship 
from src.api.config.database import Base

class Course(Base):    
    __tablename__ = "courses"    

    code                = Column(Integer, primary_key=True, autoincrement=True)      
    name                = Column(String(length=60))
    credits             = Column(Integer)
    type                = Column(String(length=60))

    group = relationship("Group", back_populates="course")