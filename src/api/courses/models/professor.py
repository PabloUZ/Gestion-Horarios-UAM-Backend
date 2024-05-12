from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import relationship 
from src.api.config.database import Base

class Professor(Base):    
    __tablename__ = "proffesors"    

    id                = Column(Integer, primary_key=True, autoincrement=True)      
    name                = Column(String(length=60))

    groups = relationship("Group", back_populates="professor")
    