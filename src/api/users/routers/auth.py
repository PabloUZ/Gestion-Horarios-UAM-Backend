from fastapi import APIRouter, Body

from src.api.users.schemas.users import Login
from src.api.users.repositories.auth import handle_login

router = APIRouter(prefix="/auth")

@router.post('/login')
def login(payload: Login = Body()):
    return handle_login(payload)