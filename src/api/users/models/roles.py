from sqlalchemy import Boolean, Column, String
from sqlalchemy.orm import relationship
from src.api.users.models.role_permissions import role_permissions
from src.api.config.database import Base


class Role(Base):
    __tablename__ = "roles"
    name = Column(String(length=50), primary_key=True)
    description = Column(String(length=250))
    active = Column(Boolean, default=False)

    permissions = relationship("Permission", secondary=role_permissions, back_populates="roles", passive_deletes=True)
    users = relationship("User", back_populates="role", passive_deletes=True)