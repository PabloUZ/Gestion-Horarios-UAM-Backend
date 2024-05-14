from fastapi import APIRouter, Body, Depends, Path, Query, Request
from typing import Optional

from src.api.middlewares.has_permission import HasPermission
from src.api.middlewares.has_access import has_access
from src.api.users.schemas.users import ChangePassword, CreateUser, UpdateUser
from src.api.users.repositories.users import add_roles, change_password, delete_user, get_single, post_user, get_all_users, remove_roles, update_user

router = APIRouter(prefix="/users")


@router.post('', dependencies=[Depends(has_access), Depends(HasPermission("CREATE_USER"))])
def create_user(user: CreateUser = Body()):
    return post_user(user)

@router.get('', dependencies=[Depends(has_access), Depends(HasPermission("GET_ALL_USERS"))])
def list_users(email: Optional[str] = Query(default=None), active: Optional[str] = Query(default=None), first_name: Optional[str] = Query(default=None), last_name: Optional[str] = Query(default=None)):
    return get_all_users(email, active, first_name, last_name)

@router.get('/{cc}', dependencies=[Depends(has_access), Depends(HasPermission("GET_SINGLE_USER", True))])
def user_detail(cc = Path()):
    return get_single(cc)

@router.put('/{cc}', dependencies=[Depends(has_access), Depends(HasPermission("UPDATE_USER", True))])
def update_user(cc = Path(), user: UpdateUser = Body()):
    return update_user(cc, user)

@router.patch('/{cc}/password', dependencies=[Depends(has_access), Depends(HasPermission("UPDATE_USER", True))])
def update_user_password(cc = Path(), payload: ChangePassword = Body()):
    return change_password(cc, payload.password)

@router.delete('/{cc}', dependencies=[Depends(has_access), Depends(HasPermission("DELETE_USER"))])
def delete(cc = Path()):
    return delete_user(cc)

@router.put('/{cc}/role', dependencies=[Depends(has_access), Depends(HasPermission("CHANGE_USER_ROLE"))])
def change_role(cc = Path(), payload = Body()):
    return add_roles(cc, payload["role"])

@router.delete('/{cc}/role', dependencies=[Depends(has_access), Depends(HasPermission("CHANGE_USER_ROLE"))])
def delete_role(cc = Path()):
    return remove_roles(cc)
