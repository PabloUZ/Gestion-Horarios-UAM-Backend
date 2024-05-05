from sqlalchemy import Boolean, Column, String
from src.api.config.database import Base


class User(Base):
    __tablename__ = "users"
    cc = Column(String(length=10), primary_key=True)
    email = Column(String(length=80), unique=True, index=True)
    first_name = Column(String(length=50))
    last_name = Column(String(length=50))
    password = Column(String(length=250))
    active = Column(Boolean, default=False)