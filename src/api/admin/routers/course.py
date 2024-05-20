from fastapi import APIRouter, Depends
from src.scrapping.administrator import Administrator
from src.api.admin.repositories.course import CourseAdminRepository
from fastapi.responses import JSONResponse
from src.api.config.database import SessionLocal

from src.api.middlewares.has_permission import HasPermission
from src.api.middlewares.has_access import has_access


router = APIRouter(prefix='/admin/courses')




@router.post('/scrapping', dependencies=[Depends(has_access), Depends(HasPermission("POST_COURSE_SCRAPPING"))])
def generate_courses_scrapping(year: int, period: int):
    admin = Administrator()
    admin.set_scrapping_period(year=year, period=period)
    courses = admin.generate_courses()
    db = SessionLocal()
    CourseAdminRepository(db).add_courses(courses)
    return JSONResponse(content=courses, status_code=201)