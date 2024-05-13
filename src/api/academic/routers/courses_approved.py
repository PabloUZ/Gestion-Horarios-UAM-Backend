from fastapi import APIRouter
from src.api.academic.schemas.courses_approved import CoursesApproved
from src.api.academic.repositories.courses_approved import CourseApprovedRepository
from fastapi import Body, Path
from fastapi.responses import JSONResponse
from typing import List
from fastapi.encoders import jsonable_encoder
from src.api.config.database import SessionLocal
from src.api.academic.models.courses_approved import CourseApproved as CoursesApprovedModel
from fastapi.encoders import jsonable_encoder
from fastapi.params import Query
from fastapi import status
router = APIRouter(prefix="/courses_approved", tags=["Courses Approved"])

@router.get("/", response_model=List[CoursesApproved], description="Get all courses approved")
def get_courses_approved(offset:int = Query(default=None,min = 0), limit:int = Query(default=None,min = 1)) -> List[CoursesApproved]:
    db = SessionLocal()
    courses_approved = CourseApprovedRepository(db).get_courses_approved(offset,limit)
    return JSONResponse(content=jsonable_encoder(courses_approved), status_code=status.HTTP_200_OK)

@router.get("/{course_id}/{academic_history_id}", response_model=CoursesApproved, description="Get a course approved by id")
def get_course_approved(course_id: int = Path(ge=1), academic_history_id: int = Path(ge=1)) -> CoursesApproved:
    db = SessionLocal()
    course_approved = CourseApprovedRepository(db).get_course_approved(course_id, academic_history_id)
    if not course_approved:
        return JSONResponse(content={"message": "Course Approved not found", "data":None}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content=jsonable_encoder(course_approved), status_code=status.HTTP_200_OK)

@router.post("/", response_model=CoursesApproved, description="Create a new course approved")
def create_course_approved(course_approved: CoursesApproved = Body()) -> dict:
    db = SessionLocal()
    new_course_approved = CourseApprovedRepository(db).create_course_approved(course_approved)
    return JSONResponse(content={"message":"Course Approved created succesfully", "data": jsonable_encoder(new_course_approved)}, status_code=status.HTTP_201_CREATED)

@router.put("/{course_id}/{academic_history_id}", response_model=CoursesApproved, description="Update a course approved by id")
def update_course_approved(course_id: int = Path(ge=1), academic_history_id: int = Path(ge=1), course_approved: CoursesApproved = Body()) -> dict:
    db = SessionLocal()
    upd_course_approved = CourseApprovedRepository(db).update_course_approved(course_id, academic_history_id, course_approved)
    if not upd_course_approved:
        return JSONResponse(content={"message": "Course Approved not found", "data":None}, status_code=status.HTTP_404_NOT_FOUND)
    
    return JSONResponse(content={"message":"Course Approved updated succesfully", "data": jsonable_encoder(upd_course_approved)}, status_code=status.HTTP_200_OK)

@router.delete("/{course_id}/{academic_history_id}",response_model=dict, description="Delete a course approved by id")
def delete_course_approved(course_id: int = Path(ge=1), academic_history_id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    del_course_approved = CourseApprovedRepository(db).delete_course_approved(course_id, academic_history_id)
    if not del_course_approved:
        return JSONResponse(content={"message": "Course Approved not found", "data":None}, status_code=status.HTTP_404_NOT_FOUND)
    
    return JSONResponse(content={"message":"Course Approved deleted succesfully", "data":None}, status_code=status.HTTP_200_OK)