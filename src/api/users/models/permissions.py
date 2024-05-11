from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from src.api.users.models.role_permissions import role_permissions
from src.api.config.database import Base


class Permission(Base):
    __tablename__ = "permissions"
    name = Column(String(length=50), primary_key=True)
    description = Column(String(length=250))

    roles = relationship("Role", secondary=role_permissions, back_populates="permissions", passive_deletes=True)