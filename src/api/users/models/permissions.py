from sqlalchemy import Column, String
from src.api.config.database import Base


class Permission(Base):
    __tablename__ = "permissions"
    name = Column(String(length=50), primary_key=True)
    description = Column(String(length=250))