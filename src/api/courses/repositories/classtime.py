from typing import List
from src.api.courses.schemas.classtime import Classtime
from src.api.courses.models.classtime import Classtime as ClasstimeModel
from sqlalchemy import func

class ClasstimeRepository():    
    def __init__(self, db) -> None:        
        self.db = db
    
    def get_all_classtimes(self) -> List[Classtime]: 
        query = self.db.query(ClasstimeModel)
        return query.all()
    
    def get_classtime_by_id(self, id: int ):
        element = self.db.query(ClasstimeModel).filter(ClasstimeModel.id == id).first()    
        return element

    def delete_classtime(self, id: int ) -> dict: 
        element: Classtime= self.db.query(ClasstimeModel).filter(ClasstimeModel.id == id).first()       
        self.db.delete(element)    
        self.db.commit()    
        return element

    def create_new_classtime(self, classtime:Classtime ) -> dict:
        new_classtime = ClasstimeModel(**classtime.model_dump())    
        self.db.add(new_classtime)
        self.db.commit()    
        self.db.refresh(new_classtime)
        return new_classtime
    
    def update_classtime(self, id: int, classtime: Classtime) -> dict:        
        element = self.db.query(ClasstimeModel).filter(ClasstimeModel.id == id).first()                
        element.day = classtime.day
        element.start_hour = classtime.start_hour
        element.end_hour = classtime.end_hour 
        element.start_minute = classtime.start_minute 
        element.end_minute = classtime.end_minute         
        self.db.commit()        
        self.db.refresh(element)        
        return element
