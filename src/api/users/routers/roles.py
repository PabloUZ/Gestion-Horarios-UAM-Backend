from fastapi import APIRouter, Body, Depends, Path, Query
from typing import Optional

from src.api.users.repositories.roles import delete_role, get_all_roles, get_single, post_role, update_role
from src.api.users.schemas.roles import CreateRole, UpdateRole

router = APIRouter(prefix="/roles")


@router.post('')
def create_role(role: CreateRole):
    return post_role(role)

@router.get('')
def list_roles(name: Optional[str] = Query(default=None), active: Optional[str] = Query(default=None)):
    return get_all_roles(name, active)

@router.get('/{name}')
def role_detail(name = Path()):
    return get_single(name)

@router.put('/{name}')
def update(name = Path(), role: UpdateRole = Body()):
    return update_role(name, role)

@router.delete('/{name}')
def delete(name = Path()):
    return delete_role(name)