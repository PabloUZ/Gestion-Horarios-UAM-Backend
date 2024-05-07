from sqlalchemy import Boolean, Column, String
from src.api.config.database import Base


class Role(Base):
    __tablename__ = "roles"
    name = Column(String(length=50), primary_key=True)
    description = Column(String(length=250))
    active = Column(Boolean, default=False)