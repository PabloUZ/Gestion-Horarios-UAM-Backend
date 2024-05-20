from fastapi import APIRouter, Body, Path, status
from fastapi.responses import JSONResponse
from typing import List
from src.api.courses.schemas.room import Room
from fastapi import APIRouter
from src.api.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.api.courses.repositories.room import RoomRepository

room_router = APIRouter(prefix='/rooms', tags=['rooms'])

#CRUD rooms

@room_router.get('',response_model=List[Room],description="Returns all rooms")
def get_rooms()-> List[Room]:
    db= SessionLocal()
    result = RoomRepository(db).get_all_rooms()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@room_router.get('/{id}',response_model=Room,description="Returns data of one specific room")
def get_rooms(id: int = Path(ge=1)) -> Room:
    db = SessionLocal()
    element=  RoomRepository(db).get_room_by_id(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested room was not found",            
                "data": None        }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    return JSONResponse(
        content=jsonable_encoder(element),                        
        status_code=status.HTTP_200_OK
        )

@room_router.post('',response_model=dict,description="Creates a new room")
def create_categorie(room: Room = Body()) -> dict:
    db= SessionLocal()
    new_room = RoomRepository(db).create_new_room(room)
    return JSONResponse(
        content={        
        "message": "The room was successfully created",        
        "data": jsonable_encoder(new_room)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@room_router.delete('/{id}',response_model=dict,description="Removes specific room")
def remove_rooms(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = RoomRepository(db).get_room_by_id(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested room was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    RoomRepository(db).delete_room(id)  
    return JSONResponse(
        content={        
            "message": "The room was removed successfully",        
            "data": None    
            }, 
        status_code=status.HTTP_200_OK
        )

@room_router.put('/{id}', tags=['rooms'], response_model=dict, description="Updates the data of specific room") 
def update_room(id: int = Path(ge=1), room: Room = Body()) -> dict:    
    db = SessionLocal()    
    element = RoomRepository(db).get_room_by_id(id)    
    if not element:        
        return JSONResponse(
            content={            
            "message": "The requested room was not found",
            "data": None        
            }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    element = RoomRepository(db).update_room(id, room)    
    return JSONResponse(
                content={        
                    "message": "The room was successfully updated",        
                    "data": jsonable_encoder(element)    
                    }, 
                status_code=status.HTTP_200_OK
                )