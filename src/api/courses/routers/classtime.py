from fastapi import APIRouter, Depends, Body, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.api.courses.schemas.classtime import Classtime
from fastapi import APIRouter
from src.api.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.api.courses.repositories.classtime import ClasstimeRepository
from src.api.middlewares.has_permission import HasPermission
from src.api.middlewares.has_access import has_access

classtime_router = APIRouter(prefix='/classtimes', tags=['classtimes'])

#CRUD classtimes

@classtime_router.get('',response_model=List[Classtime],description="Returns all classtimes")
def get_classtimes()-> List[Classtime]:
    db= SessionLocal()
    result = ClasstimeRepository(db).get_all_classtimes()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@classtime_router.get('/{id}',response_model=Classtime,description="Returns data of one specific classtime")
def get_classtimes(id: int = Path(ge=1)) -> Classtime:
    db = SessionLocal()
    element=  ClasstimeRepository(db).get_classtime_by_id(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested classtime was not found",            
                "data": None        }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    return JSONResponse(
        content=jsonable_encoder(element),                        
        status_code=status.HTTP_200_OK
        )

@classtime_router.post('',response_model=dict,description="Creates a new classtime", dependencies=[Depends(has_access), Depends(HasPermission("CREATE_CLASSTIME"))])
def create_categorie(classtime: Classtime = Body()) -> dict:
    db= SessionLocal()
    new_classtime = ClasstimeRepository(db).create_new_classtime(classtime)
    return JSONResponse(
        content={        
        "message": "The classtime was successfully created",        
        "data": jsonable_encoder(new_classtime)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@classtime_router.delete('/{id}',response_model=dict,description="Removes specific classtime", dependencies=[Depends(has_access), Depends(HasPermission("DELETE_CLASSTIME"))])
def remove_classtimes(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = ClasstimeRepository(db).get_classtime_by_id(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested classtime was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    ClasstimeRepository(db).delete_classtime(id)  
    return JSONResponse(
        content={        
            "message": "The classtime was removed successfully",        
            "data": None    
            }, 
        status_code=status.HTTP_200_OK
        )

@classtime_router.put('/{id}', tags=['classtimes'], response_model=dict, description="Updates the data of specific classtime", dependencies=[Depends(has_access), Depends(HasPermission("UPDATE_CLASSTIME"))]) 
def update_classtime(id: int = Path(ge=1), classtime: Classtime = Body()) -> dict:    
    db = SessionLocal()    
    element = ClasstimeRepository(db).get_classtime_by_id(id)    
    if not element:        
        return JSONResponse(
            content={            
            "message": "The requested classtime was not found",
            "data": None        
            }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    element = ClasstimeRepository(db).update_classtime(id, classtime)    
    return JSONResponse(
                content={        
                    "message": "The classtime was successfully updated",        
                    "data": jsonable_encoder(element)    
                    }, 
                status_code=status.HTTP_200_OK
                )
