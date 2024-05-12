from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship 
from src.api.config.database import Base

class Classtime(Base):    
    __tablename__ = "classtimes"    

    id                  = Column(Integer, primary_key=True, autoincrement=True)      
    day                 = Column(String(length=60))
    start_hour          = Column(String(length=60))
    end_hour            = Column(String(length=60))
    start_minute        = Column(String(length=60))
    end_minute          = Column(String(length=60))
    group_id = Column(Integer, ForeignKey(''))

    group = relationship("Group", back_populates="classtime")
    room = relationship("Room", back_populates="classtime")