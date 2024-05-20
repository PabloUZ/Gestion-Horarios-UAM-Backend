from typing import List
from src.api.courses.schemas.room import Room
from src.api.courses.models.room import Room as RoomModel
from sqlalchemy import func

class RoomRepository():    
    def __init__(self, db) -> None:        
        self.db = db
    
    def get_all_rooms(self) -> List[Room]: 
        query = self.db.query(RoomModel)
        return query.all()
    
    def get_room_by_id(self, id: int ):
        element = self.db.query(RoomModel).filter(RoomModel.id == id).first()    
        return element

    def get_room_by_name(self, name: str ):
        element = self.db.query(RoomModel).filter(RoomModel.name == name).first()    
        return element

    def delete_room(self, id: int ) -> dict: 
        element: Room= self.db.query(RoomModel).filter(RoomModel.id == id).first()       
        self.db.delete(element)    
        self.db.commit()    
        return element

    def create_new_room(self, room:Room ) -> dict:
        new_room = RoomModel(**room.model_dump())    
        self.db.add(new_room)
        self.db.commit()    
        self.db.refresh(new_room)
        return new_room
    
    def update_room(self, id: int, room: Room) -> dict:        
        element = self.db.query(RoomModel).filter(RoomModel.id == id).first()                
        element.name = room.name      
        self.db.commit()        
        self.db.refresh(element)        
        return element