from fastapi import FastAPI
from os import getenv

from .middlewares.error_handler import ErrorHandler

from .config.database import Base, engine

from .users.routers.auth import router as auth_router
from .users.routers.users import router as user_router
from .users.routers.roles import router as role_router
from .users.routers.permissions import router as perm_router

from .users.models.users import User
from .users.models.roles import Role
from .users.models.permissions import Permission

from .academic.routers.faculty import router as faculty_router
from .academic.routers.program import router as program_router
from .academic.routers.academic_history import router as academic_history_router
from .academic.routers.study_plan import router as study_plan_router

from .academic.models.faculty import Faculty
from .academic.models.program import Program
from .academic.models.academic_history import AcademicHistory
from .academic.models.study_plan import StudyPlan


from .admin.routers.course import router as admin_router

from .courses.routers.room import room_router 
from .courses.routers.block import blocks_router
from .courses.routers.classtime import classtime_router
from .courses.routers.course_type import courseType_router
from .courses.routers.course import course_router
from .courses.routers.group import group_router
from .courses.routers.professor import professor_router

from .courses.models.block import Block
from .courses.models.classtime import Classtime
from .courses.models.course_type import CourseType
from .courses.models.course import Course
from .courses.models.group import Group
from .courses.models.professor import Professor
from .courses.models.room import Room

api_version = getenv("API_VERSION")

app = FastAPI(root_path=f"/api/v{api_version}")

Base.metadata.create_all(bind=engine)

#app.add_middleware(ErrorHandler)

@app.get('/')
def root():
    return {
        "status": 200,
        "message": "Hello World"
    }


app.include_router(auth_router)
app.include_router(user_router)
app.include_router(role_router)
app.include_router(perm_router)
app.include_router(faculty_router)
app.include_router(program_router)
app.include_router(academic_history_router)
app.include_router(study_plan_router)
app.include_router(admin_router)
app.include_router(room_router)
app.include_router(blocks_router)
app.include_router(classtime_router)
app.include_router(courseType_router)
app.include_router(course_router)
app.include_router(group_router)
app.include_router(professor_router)
