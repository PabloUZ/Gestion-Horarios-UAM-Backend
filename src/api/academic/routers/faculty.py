from fastapi import APIRouter, Depends
from src.api.academic.schemas.faculty import Faculty
from src.api.academic.repositories.faculty import FacultyRepository
from fastapi import Body, Path
from fastapi.responses import JSONResponse
from typing import List
from fastapi.encoders import jsonable_encoder
from src.api.config.database import SessionLocal
from src.api.academic.models.faculty import Faculty as FacultyModel
from fastapi.encoders import jsonable_encoder
from fastapi.params import Query
from fastapi import status
from src.api.middlewares.has_permission import HasPermission
router = APIRouter(prefix="/faculty", tags=["Faculty"])

@router.get("/", response_model=List[Faculty], description="Get all faculties")
def get_faculties(offset:int = Query(default=None,min = 0), limit:int = Query(default=None,min = 1)) -> List[Faculty]:
    db = SessionLocal()
    faculties = FacultyRepository(db).get_faculties(offset,limit)
    return JSONResponse(content=jsonable_encoder(faculties), status_code=status.HTTP_200_OK)

@router.get("/{faculty_id}", response_model=Faculty, description="Get a faculty by id")
def get_faculty_by_id(faculty_id: int = Path(ge=1)) -> Faculty:
    db = SessionLocal()
    faculty = FacultyRepository(db).get_faculty(faculty_id)
    if not faculty:
        return JSONResponse(content={"message": "Faculty not found", "data":None}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content=jsonable_encoder(faculty), status_code=status.HTTP_200_OK)

@router.post("/", dependencies=[Depends(HasPermission("CREATE_FACULTY"))] , response_model=Faculty, description="Create a new faculty")
def create_faculty(faculty: Faculty = Body()) -> dict:
    db = SessionLocal()
    new_faculty = FacultyRepository(db).create_faculty(faculty)
    return JSONResponse(content={"message":"Faculty created succesfully", "data": jsonable_encoder(new_faculty)}, status_code=status.HTTP_201_CREATED)

@router.put("/{faculty_id}", dependencies=[Depends(HasPermission("UPDATE_FACULTY"))] , response_model=Faculty, description="Update a faculty by id")
def update_faculty(faculty_id: int = Path(ge=1), faculty: Faculty = Body()) -> dict:
    db = SessionLocal()
    upd_faculty = FacultyRepository(db).get_faculty(faculty_id)
    if not upd_faculty:
        return JSONResponse(content={"message": "Faculty not found", "data":None}, status_code=status.HTTP_404_NOT_FOUND)
    
    upd_faculty = FacultyRepository(db).update_faculty(faculty_id, faculty)
    return JSONResponse(content={"message":"Faculty updated succesfully", "data": jsonable_encoder(upd_faculty)}, status_code=status.HTTP_200_OK)

@router.delete("/{faculty_id}", dependencies=[Depends(HasPermission("DELETE_FACULTY"))] ,response_model=dict, description="Delete a faculty by id")
def delete_faculty(faculty_id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    del_faculty = FacultyRepository(db).get_faculty(faculty_id)
    if not del_faculty:
        return JSONResponse(content={"message": "Faculty not found", "data":None}, status_code=status.HTTP_404_NOT_FOUND)
    
    FacultyRepository(db).delete_faculty(faculty_id)
    return JSONResponse(content={"message":"Faculty deleted succesfully", "data":None}, status_code=status.HTTP_200_OK)