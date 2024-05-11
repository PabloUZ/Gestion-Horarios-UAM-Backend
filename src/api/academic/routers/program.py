from fastapi import APIRouter
from src.api.academic.schemas.program import Program
from src.api.academic.repositories.program import ProgramRepository
from fastapi import Body, Path
from fastapi.responses import JSONResponse
from typing import List
from fastapi.encoders import jsonable_encoder
from src.api.config.database import SessionLocal
from src.api.academic.models.program import Program as ProgramModel
from fastapi.encoders import jsonable_encoder
from fastapi.params import Query
from fastapi import status
router = APIRouter(prefix="/program", tags=["Program"])

@router.get("/", response_model=List[Program], description="Get all programs")
def get_programs(offset:int = Query(default=None,min = 0), limit:int = Query(default=None,min = 1)) -> List[Program]:
    db = SessionLocal()
    programs = ProgramRepository(db).get_programs(offset,limit)
    return JSONResponse(content=jsonable_encoder(programs), status_code=status.HTTP_200_OK)

@router.get("/{program_id}", response_model=Program, description="Get a program by id")
def get_program_by_id(program_id: int = Path(ge=1)) -> Program:
    db = SessionLocal()
    program = ProgramRepository(db).get_program(program_id)
    if not program:
        return JSONResponse(content={"message": "Program not found", "data":None}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content=jsonable_encoder(program), status_code=status.HTTP_200_OK)

@router.post("/", response_model=Program, description="Create a new program")
def create_program(program: Program = Body()) -> dict:
    db = SessionLocal()
    new_program = ProgramRepository(db).create_program(program)
    return JSONResponse(content={"message":"Program created succesfully", "data": jsonable_encoder(new_program)}, status_code=status.HTTP_201_CREATED)

@router.put("/{program_id}", response_model=Program, description="Update a program by id")
def update_program(program_id: int = Path(ge=1), program: Program = Body()) -> dict:
    db = SessionLocal()
    upd_program = ProgramRepository(db).get_program(program_id)
    if not upd_program:
        return JSONResponse(content={"message": "Program not found", "data":None}, status_code=status.HTTP_404_NOT_FOUND)
    
    upd_program = ProgramRepository(db).update_program(program_id, program)
    return JSONResponse(content={"message":"Program updated succesfully", "data": jsonable_encoder(upd_program)}, status_code=status.HTTP_200_OK)

@router.delete("/{program_id}",response_model=dict, description="Delete a program by id")
def delete_program(program_id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    del_program = ProgramRepository(db).get_program(program_id)
    if not del_program:
        return JSONResponse(content={"message": "Program not found", "data":None}, status_code=status.HTTP_404_NOT_FOUND)
    
    ProgramRepository(db).delete_program(program_id)
    return JSONResponse(content={"message":"Program deleted succesfully", "data":None}, status_code=status.HTTP_200_OK)