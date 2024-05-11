from fastapi import APIRouter, Body, Depends, Path, Query
from typing import Optional

from src.api.users.repositories.permissions import delete_permission, get_all_permissions, get_single, post_permission, update_permission
from src.api.users.schemas.permissions import CreatePermission, UpdatePermission

router = APIRouter(prefix="/permissions")


@router.post('')
def create_perm(perm: CreatePermission):
    return post_permission(perm)

@router.get('')
def list_perms(name: Optional[str] = Query(default=None)):
    return get_all_permissions(name)

@router.get('/{name}')
def perm_detail(name = Path()):
    return get_single(name)

@router.put('/{name}')
def update(name = Path(), perm: UpdatePermission = Body()):
    return update_permission(name, perm)

@router.delete('/{name}')
def delete(name = Path()):
    return delete_permission(name)