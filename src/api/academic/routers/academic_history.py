from fastapi import APIRouter, Depends
from src.api.academic.schemas.academic_history import AcademicHistory
from src.api.academic.repositories.academic_history import AcademicHistoryRepository
from fastapi import Body, Path
from fastapi.responses import JSONResponse
from typing import List
from fastapi.encoders import jsonable_encoder
from src.api.config.database import SessionLocal
from src.api.academic.models.academic_history import AcademicHistory as AcademicHistoryModel
from fastapi.encoders import jsonable_encoder
from fastapi.params import Query
from fastapi import status
from src.api.middlewares.has_permission import HasPermission
from src.api.middlewares.has_access import has_access
router = APIRouter(prefix="/academic_history", tags=["Academic History"])

@router.get("/", dependencies=[Depends(HasPermission("GET_ALL_ACADEMIC_HISTORIES"))] , response_model=List[AcademicHistory], description="Get all academic histories")
def get_academic_histories(offset:int = Query(default=None,min = 0), limit:int = Query(default=None,min = 1)) -> List[AcademicHistory]:
    db = SessionLocal()
    academic_histories = AcademicHistoryRepository(db).get_academic_histories(offset,limit)
    return JSONResponse(content=jsonable_encoder(academic_histories), status_code=status.HTTP_200_OK)

@router.get("/{academic_history_id}", dependencies=[Depends(has_access),Depends(HasPermission("GET_ACADEMIC_HISTORY"))] ,response_model=AcademicHistory, description="Get a academic history by id")
def get_academic_history_by_id(academic_history_id: int = Path(ge=1)) -> AcademicHistory:
    db = SessionLocal()
    academic_history = AcademicHistoryRepository(db).get_academic_history(academic_history_id)
    if not academic_history:
        return JSONResponse(content={"message": "Academic History not found", "data":None}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content=jsonable_encoder(academic_history), status_code=status.HTTP_200_OK)

@router.post("/", dependencies=[Depends(has_access),Depends(HasPermission("CREATE_ACADEMIC_HISTORY"))] , response_model=AcademicHistory, description="Create a new academic history")
def create_academic_history(academic_history: AcademicHistory = Body()) -> dict:
    db = SessionLocal()
    new_academic_history = AcademicHistoryRepository(db).create_academic_history(academic_history)
    return JSONResponse(content={"message":"Academic History created succesfully", "data": jsonable_encoder(new_academic_history)}, status_code=status.HTTP_201_CREATED)

@router.put("/{academic_history_id}", dependencies=[Depends(has_access),Depends(HasPermission("UPDATE_ACADEMIC_HISTORY"))] , response_model=AcademicHistory, description="Update a academic history by id")
def update_academic_history(academic_history_id: int = Path(ge=1), academic_history: AcademicHistory = Body()) -> dict:
    db = SessionLocal()
    upd_academic_history = AcademicHistoryRepository(db).get_academic_history(academic_history_id)
    if not upd_academic_history:
        return JSONResponse(content={"message": "Academic History not found", "data":None}, status_code=status.HTTP_404_NOT_FOUND)
    
    upd_academic_history = AcademicHistoryRepository(db).update_academic_history(academic_history_id, academic_history)
    return JSONResponse(content={"message":"Academic History updated succesfully", "data": jsonable_encoder(upd_academic_history)}, status_code=status.HTTP_200_OK)

@router.delete("/{academic_history_id}", dependencies=[Depends(has_access),Depends(HasPermission("DELETE_ACADEMIC_HISTORY"))] ,response_model=dict, description="Delete a academic history by id")
def delete_academic_history(academic_history_id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    del_academic_history = AcademicHistoryRepository(db).get_academic_history(academic_history_id)
    if not del_academic_history:
        return JSONResponse(content={"message": "Academic History not found", "data":None}, status_code=status.HTTP_404_NOT_FOUND)
    
    AcademicHistoryRepository(db).delete_academic_history(academic_history_id)
    return JSONResponse(content={"message":"Academic History deleted succesfully", "data":None}, status_code=status.HTTP_200_OK)