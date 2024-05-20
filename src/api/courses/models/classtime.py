from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship 
from src.api.config.database import Base

class Classtime(Base):    
    __tablename__ = "classtimes"    

    id                  = Column(Integer, primary_key=True, autoincrement=True)      
    day                 = Column(String(length=60))
    start_hour          = Column(Integer)
    end_hour            = Column(Integer)
    start_minute        = Column(Integer)
    end_minute          = Column(Integer)
    group_id = Column(Integer, ForeignKey('groups.id'), nullable=False)
    room_id = Column(Integer, ForeignKey('rooms.id'), nullable=True)

    group = relationship("Group", back_populates="classtimes")
    room = relationship("Room", back_populates="classtimes")