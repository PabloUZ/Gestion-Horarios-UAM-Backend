from sqlalchemy import Boolean, Column, ForeignKey, String
from sqlalchemy.orm import relationship
from src.api.config.database import Base


class User(Base):
    __tablename__ = "users"
    cc = Column(String(length=10), primary_key=True)
    email = Column(String(length=80), unique=True, index=True)
    first_name = Column(String(length=50))
    last_name = Column(String(length=50))
    password = Column(String(length=250))
    active = Column(Boolean, default=False)
    role_name = Column('role', String(length=50), ForeignKey('roles.name', ondelete='SET NULL'))

    role = relationship("Role", back_populates="users", passive_deletes=True)