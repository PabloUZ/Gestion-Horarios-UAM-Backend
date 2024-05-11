from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy import func
from src.api.config.database import SessionLocal
from src.api.users.models.permissions import Permission

def find_by_name(name):
    db = SessionLocal()
    perm = db.query(Permission).filter(Permission.name == name).first()
    return perm

def save_permission(permission):
    db = SessionLocal()
    new_perm = Permission(**permission.model_dump())
    db.add(new_perm)
    db.commit()
    db.refresh(new_perm)
    return new_perm

def post_permission(permission):
    db = SessionLocal()
    old = db.query(Permission).filter(Permission.name == permission.name).first()
    if old:
        return JSONResponse({
            "status": 400,
            "message": "Permission already exists"
        }, 400)
    new = save_permission(permission)
    return JSONResponse({
        "status": 201,
        "message": "Permission created successfully",
        "permission": jsonable_encoder(new)
    }, 201)

def get_all_permissions(name = None):
    db = SessionLocal()
    perms = db.query(Permission)
    if name:
        perms = perms.filter(func.upper(Permission.name).ilike("%" + name.upper() + "%"))
    return JSONResponse(jsonable_encoder(perms.all()), 200)

def get_single(name):
    db = SessionLocal()
    perm = db.query(Permission).filter(Permission.name == name).first()
    if not perm:
        return JSONResponse({
            "status": 404,
            "message": "Permission not found"
        }, 404)
    return JSONResponse(jsonable_encoder(perm))

def update_permission(name, payload):
    db = SessionLocal()
    perm = db.query(Permission).filter(Permission.name == name).first()
    if not perm:
        return JSONResponse({
            "status": 404,
            "message": "Permission not found"
        }, 404)
    perm.description = payload.description
    db.commit()
    db.refresh(perm)
    return JSONResponse({
        "status": 200,
        "message": "Permission updated successfully",
        "permission": jsonable_encoder(perm)
    }, 200)

def delete_permission(name):
    db = SessionLocal()
    perm = db.query(Permission).filter(Permission.name == name).first()
    if not perm:
        return JSONResponse({
            "status": 404,
            "message": "Permission not found"
        }, 404)
    db.delete(perm)
    db.commit()
    return JSONResponse({
        "status": 200,
        "message": "Permission deleted successfully",
        "permission": jsonable_encoder(perm)
    }, 200)