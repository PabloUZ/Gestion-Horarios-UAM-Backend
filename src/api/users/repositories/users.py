from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy import func
from src.api.config.database import SessionLocal
from src.api.users.models.users import User
from src.api.utils.password import Password

def list_all_users():
    db = SessionLocal()
    return db.query(User)

def find_by_cc(cc):
    return list_all_users().filter(User.cc == cc).first()

def find_by_email(email):
    return list_all_users().filter(User.email == email).first()

def user_existent_params(user):
    existent = None
    old = find_by_cc(user.cc)
    if old is not None:
        if existent is None:
            existent = {
                "params": []
            }
        existent["params"].append("cc")
    old = find_by_email(user.email)
    if old is not None:
        if existent is None:
            existent = {
                "params": []
            }
        existent["params"].append("email")
    return existent

def save_user(user):
    db = SessionLocal()
    new_user = User(**user.model_dump())
    new_user.password = Password.hash(new_user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def post_user(user):
    error = user_existent_params(user)
    if error is not None:
        return JSONResponse({
            "status": 400,
            "message": "Unique field values encountered",
            "detail": error
        }, 400)
    new = save_user(user)
    return JSONResponse({
        "status": 201,
        "message": "User created successfully",
        "user": jsonable_encoder(new)
    }, 201)

def get_all_users(email = None, active = None, f_name = None, l_name = None):
    users = list_all_users()
    if email:
        users = users.filter(User.email == email)
    if active:
        if active == "true":
            users = users.filter(User.active)
        elif active == "false":
            users = users.filter(User.active == False)
        else:
            return JSONResponse({
                "status": 400,
                "message": "Invalid query value",
                "detail": [active]
            }, 400)
    if f_name:
        users = users.filter(func.lower(User.first_name).ilike("%" + f_name.lower() + "%"))
    if l_name:
        users = users.filter(func.lower(User.last_name).ilike("%" + l_name.lower() + "%"))
    return JSONResponse(jsonable_encoder(users.all()), 200)

def get_single(cc):
    user = find_by_cc(cc)
    if not user:
        return JSONResponse({
            "status": 404,
            "message": "User not found"
        }, 404)
    return JSONResponse(jsonable_encoder(user))

def update_user(cc, payload):
    db = SessionLocal()
    user = db.query(User).filter(User.cc == cc).first()
    if not user:
        return JSONResponse({
            "status": 404,
            "message": "User not found"
        }, 404)
    if payload.email != user.email:
        if find_by_email(payload.email) is not None:
            return JSONResponse({
                "status": 400,
                "message": "Unique field values encountered",
                "detail": ["email"]
            }, 400)
    user.email = payload.email
    user.first_name = payload.first_name
    user.last_name = payload.last_name
    user.active = payload.active
    db.commit()
    db.refresh(user)
    return JSONResponse({
        "status": 200,
        "message": "User updated successfully",
        "user": jsonable_encoder(user)
    }, 200)

def delete_user(cc):
    db = SessionLocal()
    user = db.query(User).filter(User.cc == cc).first()
    if not user:
        return JSONResponse({
            "status": 404,
            "message": "User not found"
        }, 404)
    db.delete(user)
    db.commit()
    return JSONResponse({
        "status": 200,
        "message": "User deleted successfully",
        "user": jsonable_encoder(user)
    }, 200)

def change_password(cc, pwd):
    db = SessionLocal()
    user = db.query(User).filter(User.cc == cc).first()
    if not user:
        return JSONResponse({
            "status": 404,
            "message": "User not found"
        }, 404)
    if Password.compare(pwd, user.password):
        return JSONResponse({
            "status": 400,
            "message": "The new password must be different than the current"
        }, 400)
    user.password = Password.hash(pwd)
    db.commit()
    db.refresh(user)
    return JSONResponse({
        "status": 200,
        "message": "User password updated successfully",
        "user": jsonable_encoder(user)
    }, 200)