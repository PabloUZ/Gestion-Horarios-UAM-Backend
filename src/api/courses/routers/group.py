from fastapi import APIRouter, Body, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.api.courses.schemas.group import Group
from fastapi import APIRouter
from src.api.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.api.courses.repositories.group import GroupRepository

group_router = APIRouter(prefix='/groups', tags=['groups'])

#CRUD groups

@group_router.get('',response_model=List[Group],description="Returns all groups")
def get_groups()-> List[Group]:
    db= SessionLocal()
    result = GroupRepository(db).get_all_groups()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@group_router.get('{id}',response_model=Group,description="Returns data of one specific group")
def get_groups(id: int = Path(ge=1)) -> Group:
    db = SessionLocal()
    element=  GroupRepository(db).get_group_by_id(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested group was not found",            
                "data": None        }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    return JSONResponse(
        content=jsonable_encoder(element),                        
        status_code=status.HTTP_200_OK
        )

@group_router.post('',response_model=dict,description="Creates a new group")
def create_categorie(group: Group = Body()) -> dict:
    db= SessionLocal()
    new_group = GroupRepository(db).create_new_group(group)
    return JSONResponse(
        content={        
        "message": "The group was successfully created",        
        "data": jsonable_encoder(new_group)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@group_router.delete('{id}',response_model=dict,description="Removes specific group")
def remove_groups(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = GroupRepository(db).get_group_by_id(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested group was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    GroupRepository(db).delete_group(id)  
    return JSONResponse(
        content={        
            "message": "The group was removed successfully",        
            "data": None    
            }, 
        status_code=status.HTTP_200_OK
        )

@group_router.put('/{id}', tags=['groups'], response_model=dict, description="Updates the data of specific group") 
def update_group(id: int = Path(ge=1), group: Group = Body()) -> dict:    
    db = SessionLocal()    
    element = GroupRepository(db).get_group_by_id(id)    
    if not element:        
        return JSONResponse(
            content={            
            "message": "The requested group was not found",
            "data": None        
            }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    element = GroupRepository(db).update_group(id, group)    
    return JSONResponse(
                content={        
                    "message": "The group was successfully updated",        
                    "data": jsonable_encoder(element)    
                    }, 
                status_code=status.HTTP_200_OK
                )