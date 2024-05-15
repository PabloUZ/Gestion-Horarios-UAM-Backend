from fastapi import File, UploadFile, APIRouter
from fastapi.responses import JSONResponse
import json

from src.api.users.schemas.users import CreateUser
from src.api.users.schemas.permissions import CreatePermission
from src.api.users.schemas.roles import CreateRole
from src.api.users.models.roles import Role
from src.api.users.repositories.users import add_roles, post_user
from src.api.users.repositories.roles import add_perms, post_role
from src.api.users.repositories.permissions import post_permission
from src.api.config.database import SessionLocal

router = APIRouter(prefix="/init")


@router.post('/init-data')
async def init(file: UploadFile = File()):
    db = SessionLocal()
    r = db.query(Role).filter(Role.name == "ROOT").first()
    if r is not None:
        return JSONResponse({
            "status": 403,
            "message": "System was already initialized"
        })
    content = await file.read()

    if file.content_type != "application/json":
        return JSONResponse({
            "status": 400,
            "message": "File is not JSON"
        })
    print(content)
    try:
        data = json.loads(content)
    except:
        return JSONResponse({
            "status": 400,
            "message": "Invalid JSON format"
        })
    for permission in data["permissions"]:
        post_permission(CreatePermission(
            name=permission["name"],
            description=permission["description"]))
    for role in data["roles"]:
        post_role(CreateRole(
            name=role["creation"]["name"],
            description=role["creation"]["description"],
            active=role["creation"]["active"]
        ))
        add_perms(role["creation"]["name"], role["permissions"])
    post_user(CreateUser(
        cc=data["user"]["cc"],
        email=data["user"]["email"],
        first_name=data["user"]["first_name"],
        last_name=data["user"]["last_name"],
        password=data["user"]["password"],
        active=data["user"]["active"]
    ))
    add_roles(data["user"]["cc"], "ROOT")
    return JSONResponse({
        "status": 200,
        "message": "System initialization success"
    })