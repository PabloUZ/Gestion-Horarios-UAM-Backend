from sqlalchemy import Boolean, Column, Integer, String 
from sqlalchemy.orm import relationship 
from src.api.config.database import Base

class Block(Base):    
    __tablename__ = "blocks"    

    id              = Column(Integer, primary_key=True, autoincrement=True)      
    name            = Column(String(length=60))
    prefix = Column(String(length=5))

    rooms = relationship("Room", back_populates="block")
