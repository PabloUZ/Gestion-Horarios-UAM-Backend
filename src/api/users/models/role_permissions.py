from sqlalchemy import Table, Column, String, ForeignKey
from src.api.config.database import Base

role_permissions = Table('role_permissions', Base.metadata,
    Column('role_name', String(length=50), ForeignKey('roles.name', ondelete='CASCADE')),
    Column('permission_name', String(length=50), ForeignKey('permissions.name', ondelete='CASCADE'))
)