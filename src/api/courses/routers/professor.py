from fastapi import APIRouter, Body, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.api.courses.schemas.professor import Professor
from fastapi import APIRouter
from src.api.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.api.courses.repositories.professor import ProfessorRepository

professor_router = APIRouter(prefix='/professors', tags=['professors'])

#CRUD professors

@professor_router.get('',response_model=List[Professor],description="Returns all professors")
def get_professors()-> List[Professor]:
    db= SessionLocal()
    result = ProfessorRepository(db).get_all_professors()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@professor_router.get('/{id}',response_model=Professor,description="Returns data of one specific professor")
def get_professors(id: int = Path(ge=1)) -> Professor:
    db = SessionLocal()
    element=  ProfessorRepository(db).get_professor_by_id(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested professor was not found",            
                "data": None        }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    return JSONResponse(
        content=jsonable_encoder(element),                        
        status_code=status.HTTP_200_OK
        )

@professor_router.post('',response_model=dict,description="Creates a new professor")
def create_categorie(professor: Professor = Body()) -> dict:
    db= SessionLocal()
    new_professor = ProfessorRepository(db).create_new_professor(professor)
    return JSONResponse(
        content={        
        "message": "The professor was successfully created",        
        "data": jsonable_encoder(new_professor)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@professor_router.delete('/{id}',response_model=dict,description="Removes specific professor")
def remove_professors(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = ProfessorRepository(db).get_professor_by_id(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested professor was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    ProfessorRepository(db).delete_professor(id)  
    return JSONResponse(
        content={        
            "message": "The professor was removed successfully",        
            "data": None    
            }, 
        status_code=status.HTTP_200_OK
        )

@professor_router.put('/{id}', tags=['professors'], response_model=dict, description="Updates the data of specific professor") 
def update_professor(id: int = Path(ge=1), professor: Professor = Body()) -> dict:    
    db = SessionLocal()    
    element = ProfessorRepository(db).get_professor_by_id(id)    
    if not element:        
        return JSONResponse(
            content={            
            "message": "The requested professor was not found",
            "data": None        
            }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    element = ProfessorRepository(db).update_professor(id, professor)    
    return JSONResponse(
                content={        
                    "message": "The professor was successfully updated",        
                    "data": jsonable_encoder(element)    
                    }, 
                status_code=status.HTTP_200_OK
                )