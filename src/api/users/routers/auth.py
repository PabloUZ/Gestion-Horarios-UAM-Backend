from fastapi import APIRouter, Body

from src.api.users.schemas.users import Login
from src.api.users.repositories.auth import handle_login, refresh_token

router = APIRouter(prefix="/auth")

@router.post('/login')
def login(payload: Login = Body()):
    return handle_login(payload)

@router.post('/refresh-session')
def refresh_session(payload = Body()):
    return refresh_token(payload["token"])