from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.api.users.models.users import User
from src.api.config.database import SessionLocal
from src.api.utils.password import Password
from src.api.utils.jwt import JWT


def handle_login(payload):
    db = SessionLocal()
    user = db.query(User).filter(User.email == payload.email).first()
    if not user:
        return JSONResponse({
            "status": 401,
            "message": "Username or password incorrect"
        }, 401)
    if (not Password.compare(payload.password, user.password)):
        return JSONResponse({
            "status": 401,
            "message": "Username or password incorrect"
        }, 401)
    to_encode = jsonable_encoder(user)
    del to_encode['password']
    if user.role:
        to_encode['role'] = jsonable_encoder(user.role)
        to_encode['role']['permissions'] = []
        for p in jsonable_encoder(user.role.permissions):
            to_encode['role']['permissions'].append(p["name"])
    else:
        to_encode['role'] = None
    encoded = JWT.encode(to_encode, 1)
    return JSONResponse({
        "status": 200,
        "token": encoded
    }, 200)

def refresh_token(token):
    to_encode = JWT.decode(token)
    encoded = JWT.encode(to_encode, 2)
    return JSONResponse({
        "status": 200,
        "token": encoded
    }, 200)
# @router.post('/register')
# def handle_register(payload = Body()):
#     pass