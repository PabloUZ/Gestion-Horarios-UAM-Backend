from fastapi import APIRouter, Body, Depends, Path, Query
from typing import Optional

from src.api.users.repositories.roles import add_perms, delete_perm, delete_role, get_all_roles, get_single, list_perms, post_role, update_role
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

@router.get('/{name}/permissions')
def list_permissions(name = Path()):
    return list_perms(name)

@router.post('/{name}/permissions')
def add_permissions(name = Path(), perms = Body()):
    return add_perms(name, perms)

@router.delete('/{name}/permissions/{perm_name}')
def remove_permission(name = Path(), perm_name = Path()):
    return delete_perm(name, perm_name)