from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy import func
from src.api.config.database import SessionLocal
from src.api.users.models.roles import Role

def find_by_name(name):
    db = SessionLocal()
    role = db.query(Role).filter(Role.name == name).first()
    return role

def save_role(role):
    db = SessionLocal()
    new_role = Role(**role.model_dump())
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return new_role

def post_role(role):
    db = SessionLocal()
    old = db.query(Role).filter(Role.name == role.name).first()
    if old:
        return JSONResponse({
            "status": 400,
            "message": "Role already exists"
        }, 400)
    new = save_role(role)
    return JSONResponse({
        "status": 201,
        "message": "Role created successfully",
        "role": jsonable_encoder(new)
    }, 201)

def get_all_roles(name = None, active = None):
    db = SessionLocal()
    roles = db.query(Role)
    if name:
        roles = roles.filter(func.upper(Role.name).ilike("%" + name.upper() + "%"))
    if active:
        if active == "true":
            roles = roles.filter(Role.active)
        elif active == "false":
            roles = roles.filter(Role.active == False)
        else:
            return JSONResponse({
                "status": 400,
                "message": "Invalid query value",
                "detail": [active]
            }, 400)
    return JSONResponse(jsonable_encoder(roles.all()), 200)

def get_single(name):
    db = SessionLocal()
    role = db.query(Role).filter(Role.name == name).first()
    if not role:
        return JSONResponse({
            "status": 404,
            "message": "Role not found"
        }, 404)
    return JSONResponse(jsonable_encoder(role))

def update_role(name, payload):
    db = SessionLocal()
    role = db.query(Role).filter(Role.name == name).first()
    if not role:
        return JSONResponse({
            "status": 404,
            "message": "Role not found"
        }, 404)
    if role.name == "ROOT":
        return JSONResponse({
            "status": 400,
            "message": "ROOT role can't be updated"
        }, 400)
    role.description = payload.description
    role.active = payload.active
    db.commit()
    db.refresh(role)
    return JSONResponse({
        "status": 200,
        "message": "Role updated successfully",
        "role": jsonable_encoder(role)
    }, 200)

def delete_role(name):
    db = SessionLocal()
    role = db.query(Role).filter(Role.name == name).first()
    if not role:
        return JSONResponse({
            "status": 404,
            "message": "Role not found"
        }, 404)
    if role.name == "ROOT":
        return JSONResponse({
            "status": 400,
            "message": "ROOT role can't be deleted"
        }, 400)
    db.delete(role)
    db.commit()
    return JSONResponse({
        "status": 200,
        "message": "Role deleted successfully",
        "role": jsonable_encoder(role)
    }, 200)