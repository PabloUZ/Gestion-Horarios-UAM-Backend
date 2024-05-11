from fastapi import APIRouter
from src.api.academic.schemas.study_plan import StudyPlan
from src.api.academic.repositories.study_plan import StudyPlanRepository
from fastapi import Body, Path
from fastapi.responses import JSONResponse
from typing import List
from fastapi.encoders import jsonable_encoder
from src.api.config.database import SessionLocal
from src.api.academic.models.study_plan import StudyPlan as StudyPlanModel
from fastapi.encoders import jsonable_encoder
from fastapi.params import Query
from fastapi import status

router = APIRouter(prefix="/study_plan", tags=["Study Plan"])

@router.get("/", response_model=List[StudyPlan], description="Get all study plans")
def get_study_plans(offset:int = Query(default=None,min = 0), limit:int = Query(default=None,min = 1)) -> List[StudyPlan]:
    db = SessionLocal()
    study_plans = StudyPlanRepository(db).get_study_plans(offset,limit)
    return JSONResponse(content=jsonable_encoder(study_plans), status_code=status.HTTP_200_OK)

@router.get("/{study_plan_id}", response_model=StudyPlan, description="Get a study plan by id")
def get_study_plan_by_id(study_plan_id: int = Path(ge=1)) -> StudyPlan:
    db = SessionLocal()
    study_plan = StudyPlanRepository(db).get_study_plan(study_plan_id)
    if not study_plan:
        return JSONResponse(content={"message": "Study Plan not found", "data":None}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content=jsonable_encoder(study_plan), status_code=status.HTTP_200_OK)

@router.post("/", response_model=StudyPlan, description="Create a new study plan")
def create_study_plan(study_plan: StudyPlan = Body()) -> dict:
    db = SessionLocal()
    new_study_plan = StudyPlanRepository(db).create_study_plan(study_plan)
    return JSONResponse(content={"message":"Study Plan created succesfully", "data": jsonable_encoder(new_study_plan)}, status_code=status.HTTP_201_CREATED)

@router.put("/{study_plan_id}", response_model=StudyPlan, description="Update a study plan by id")
def update_study_plan(study_plan_id: int = Path(ge=1), study_plan: StudyPlan = Body()) -> dict:
    db = SessionLocal()
    upd_study_plan = StudyPlanRepository(db).get_study_plan(study_plan_id)
    if not upd_study_plan:
        return JSONResponse(content={"message": "Study Plan not found", "data":None}, status_code=status.HTTP_404_NOT_FOUND)
    
    upd_study_plan = StudyPlanRepository(db).update_study_plan(study_plan_id, study_plan)
    return JSONResponse(content={"message":"Study Plan updated succesfully", "data": jsonable_encoder(upd_study_plan)}, status_code=status.HTTP_200_OK)

@router.delete("/{study_plan_id}",response_model=dict, description="Delete a study plan by id")
def delete_study_plan(study_plan_id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    del_study_plan = StudyPlanRepository(db).get_study_plan(study_plan_id)
    if not del_study_plan:
        return JSONResponse(content={"message": "Study Plan not found", "data":None}, status_code=status.HTTP_404_NOT_FOUND)
    
    StudyPlanRepository(db).delete_study_plan(study_plan_id)
    return JSONResponse(content={"message":"Study Plan deleted succesfully", "data":None}, status_code=status.HTTP_200_OK)