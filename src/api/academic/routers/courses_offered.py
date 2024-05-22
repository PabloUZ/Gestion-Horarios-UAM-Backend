from fastapi import APIRouter, Depends
from src.api.academic.schemas.courses_offered import CoursesOffered
from src.api.academic.repositories.courses_offered import CourseOfferedRepository
from fastapi import Body, Path
from fastapi.responses import JSONResponse
from typing import List
from fastapi.encoders import jsonable_encoder
from src.api.config.database import SessionLocal
from src.api.academic.models.courses_offered import CourseOffered as CoursesOfferedModel
from fastapi.encoders import jsonable_encoder
from fastapi.params import Query
from fastapi import status
from src.api.middlewares.has_permission import HasPermission
router = APIRouter(prefix="/courses_offered", tags=["Courses Offered"])

@router.get("/", response_model=List[CoursesOffered], description="Get all courses offered")
def get_courses_offered(offset:int = Query(default=None,min = 0), limit:int = Query(default=None,min = 1)) -> List[CoursesOffered]:
    db = SessionLocal()
    courses_offered = CourseOfferedRepository(db).get_courses_offered(offset,limit)
    return JSONResponse(content=jsonable_encoder(courses_offered), status_code=status.HTTP_200_OK)

@router.get("/{course_offered_id}", response_model=CoursesOffered, description="Get a course offered by id")
def get_course_offered(course_offered_id:int = Path(ge=1)) -> CoursesOffered:
    db = SessionLocal()
    course_offered = CourseOfferedRepository(db).get_course_offered(course_offered_id)
    if not course_offered:
        return JSONResponse(content={"message": "Course Offered not found", "data":None}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content=jsonable_encoder(course_offered), status_code=status.HTTP_200_OK)

@router.post("/", dependencies=[Depends(HasPermission("CREATE_COURSE_OFFERED"))] ,response_model=CoursesOffered, description="Create a new course offered")
def create_course_offered(course_offered: CoursesOffered = Body()) -> dict:
    db = SessionLocal()
    new_course_offered = CourseOfferedRepository(db).create_course_offered(course_offered)
    return JSONResponse(content={"message":"Course Offered created succesfully", "data": jsonable_encoder(new_course_offered)}, status_code=status.HTTP_201_CREATED)

@router.put("/{course_offered_id}", dependencies=[Depends(HasPermission("UPDATE_COURSE_OFFERED"))] ,response_model=CoursesOffered, description="Update a course Offered by id")
def update_course_offered(course_offered_id:int = Path(ge=1), course_offered: CoursesOffered = Body()) -> dict:
    db = SessionLocal()
    upd_course_offered = CourseOfferedRepository(db).update_course_offered(course_offered_id, course_offered)
    if not upd_course_offered:
        return JSONResponse(content={"message": "Course Offered not found", "data":None}, status_code=status.HTTP_404_NOT_FOUND)
    
    return JSONResponse(content={"message":"Course Offered updated succesfully", "data": jsonable_encoder(upd_course_offered)}, status_code=status.HTTP_200_OK)

@router.delete("/{course_offered_id}", dependencies=[Depends(HasPermission("DELETE_COURSE_OFFERED"))] , response_model=dict, description="Delete a course Offered by id")
def delete_course_offered(course_offered_id:int = Path(ge=1)) -> dict:
    db = SessionLocal()
    del_course_offered = CourseOfferedRepository(db).delete_course_offered(course_offered_id)
    if not del_course_offered:
        return JSONResponse(content={"message": "Course Offered not found", "data":None}, status_code=status.HTTP_404_NOT_FOUND)
    
    return JSONResponse(content={"message":"Course Offered deleted succesfully", "data":None}, status_code=status.HTTP_200_OK)