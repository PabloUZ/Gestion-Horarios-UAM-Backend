from fastapi import APIRouter, Body, Depends, Path, Query
from typing import Optional

from src.api.users.schemas.users import ChangePassword, CreateUser, UpdateUser
from src.api.users.repositories.users import change_password, delete_user, get_single, post_user, get_all_users, update_user

router = APIRouter(prefix="/users")


@router.post('')
def create_user(user: CreateUser = Body()):
    return post_user(user)

@router.get('')
def list_users(email: Optional[str] = Query(default=None), active: Optional[str] = Query(default=None), first_name: Optional[str] = Query(default=None), last_name: Optional[str] = Query(default=None)):
    return get_all_users(email, active, first_name, last_name)

@router.get('/{cc}')
def user_detail(cc = Path()):
    return get_single(cc)

@router.put('/{cc}')
def update_user(cc = Path(), user: UpdateUser = Body()):
    return update_user(cc, user)

@router.patch('/{cc}/password')
def update_user_password(cc = Path(), payload: ChangePassword = Body()):
    return change_password(cc, payload.password)

@router.delete('/{cc}')
def user_detail(cc = Path()):
    return delete_user(cc)