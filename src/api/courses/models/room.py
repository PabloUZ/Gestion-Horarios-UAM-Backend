from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship 
from src.api.config.database import Base

class Room(Base):    
    __tablename__ = "rooms"    

    id                = Column(Integer, primary_key=True, autoincrement=True)      
    name              = Column(String(length=60))
    block_id = Column(Integer, ForeignKey('blocks.id'))

    classtimes = relationship("Classtime", back_populates="room")
    block = relationship("Block", back_populates="rooms")