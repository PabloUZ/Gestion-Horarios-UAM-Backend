from fastapi import APIRouter, Body, Depends, Path, Query
from typing import Optional

from src.api.middlewares.has_permission import HasPermission
from src.api.middlewares.has_access import has_access
from src.api.users.repositories.permissions import delete_permission, get_all_permissions, get_single, post_permission, update_permission
from src.api.users.schemas.permissions import CreatePermission, UpdatePermission

router = APIRouter(prefix="/permissions")


@router.post('')
def create_perm(perm: CreatePermission):
    return post_permission(perm)

@router.get('', dependencies=[Depends(has_access), Depends(HasPermission("GET_ALL_PERMISSIONS"))])
def list_perms(name: Optional[str] = Query(default=None)):
    return get_all_permissions(name)

@router.get('/{name}', dependencies=[Depends(has_access), Depends(HasPermission("GET_SINGLE_PERMISSION"))])
def perm_detail(name = Path()):
    return get_single(name)

@router.put('/{name}')
def update(name = Path(), perm: UpdatePermission = Body()):
    return update_permission(name, perm)

@router.delete('/{name}')
def delete(name = Path()):
    return delete_permission(name)