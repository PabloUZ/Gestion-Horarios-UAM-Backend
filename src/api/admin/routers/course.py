from fastapi import APIRouter
from src.scrapping.administrator import Administrator
from src.api.admin.repositories.course import CourseAdminRepository
from fastapi.responses import JSONResponse
from src.api.config.database import SessionLocal
router = APIRouter(prefix='/admin/courses')

admin = Administrator()


@router.post('')
def generate_courses():
    courses = admin.generate_courses()
    db = SessionLocal()
    CourseAdminRepository(db).add_courses(courses)
    return JSONResponse(content=courses, status_code=201)