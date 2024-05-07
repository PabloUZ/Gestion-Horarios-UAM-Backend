from fastapi import FastAPI
from os import getenv

from .config.database import Base, engine

from .users.routers.users import router as user_router
from .users.routers.roles import router as role_router

from .users.models.users import User
from .users.models.roles import Role

api_version = getenv("API_VERSION")

app = FastAPI(root_path=f"/api/v{api_version}")

Base.metadata.create_all(bind=engine)


@app.get('/')
def root():
    return {
        "status": 200,
        "message": "Hello World"
    }

app.include_router(user_router)
app.include_router(role_router)