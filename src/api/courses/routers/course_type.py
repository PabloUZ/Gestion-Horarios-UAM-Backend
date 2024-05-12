from fastapi import APIRouter, Body, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.api.courses.schemas.course_type import CourseType
from fastapi import APIRouter
from src.api.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.api.courses.repositories.course_type import CourseTypeRepository

courseType_router = APIRouter(prefix='/courseTypes', tags=['courseTypes'])

#CRUD courseTypes

@courseType_router.get('',response_model=List[CourseType],description="Returns all courseTypes")
def get_courseTypes()-> List[CourseType]:
    db= SessionLocal()
    result = CourseTypeRepository(db).get_all_courseTypes()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@courseType_router.get('{id}',response_model=CourseType,description="Returns data of one specific courseType")
def get_courseTypes(id: int = Path(ge=1)) -> CourseType:
    db = SessionLocal()
    element=  CourseTypeRepository(db).get_courseType_by_id(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested courseType was not found",            
                "data": None        }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    return JSONResponse(
        content=jsonable_encoder(element),                        
        status_code=status.HTTP_200_OK
        )

@courseType_router.post('',response_model=dict,description="Creates a new courseType")
def create_categorie(courseType: CourseType = Body()) -> dict:
    db= SessionLocal()
    new_courseType = CourseTypeRepository(db).create_new_courseType(courseType)
    return JSONResponse(
        content={        
        "message": "The courseType was successfully created",        
        "data": jsonable_encoder(new_courseType)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@courseType_router.delete('{id}',response_model=dict,description="Removes specific courseType")
def remove_courseTypes(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = CourseTypeRepository(db).get_courseType_by_id(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested courseType was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    CourseTypeRepository(db).delete_courseType(id)  
    return JSONResponse(
        content={        
            "message": "The courseType was removed successfully",        
            "data": None    
            }, 
        status_code=status.HTTP_200_OK
        )

@courseType_router.put('/{id}', tags=['courseTypes'], response_model=dict, description="Updates the data of specific courseType") 
def update_courseType(id: int = Path(ge=1), courseType: CourseType = Body()) -> dict:    
    db = SessionLocal()    
    element = CourseTypeRepository(db).get_courseType_by_id(id)    
    if not element:        
        return JSONResponse(
            content={            
            "message": "The requested courseType was not found",
            "data": None        
            }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    element = CourseTypeRepository(db).update_courseType(id, courseType)    
    return JSONResponse(
                content={        
                    "message": "The courseType was successfully updated",        
                    "data": jsonable_encoder(element)    
                    }, 
                status_code=status.HTTP_200_OK
                )
