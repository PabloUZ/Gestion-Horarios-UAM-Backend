from typing import List
from src.api.courses.schemas.course_type import CourseType
from src.api.courses.models.course_type import CourseType as CourseTypeModel
from sqlalchemy import func

class CourseTypeRepository():    
    def __init__(self, db) -> None:        
        self.db = db
    
    def get_all_courseTypes(self) -> List[CourseType]: 
        query = self.db.query(CourseTypeModel)
        return query.all()
    
    def get_courseType_by_id(self, id: int ):
        element = self.db.query(CourseTypeModel).filter(CourseTypeModel.id == id).first()    
        return element

    def delete_courseType(self, id: int ) -> dict: 
        element: CourseType= self.db.query(CourseTypeModel).filter(CourseTypeModel.id == id).first()       
        self.db.delete(element)    
        self.db.commit()    
        return element

    def create_new_courseType(self, courseType:CourseType ) -> dict:
        new_courseType = CourseTypeModel(**courseType.model_dump())    
        self.db.add(new_courseType)
        self.db.commit()    
        self.db.refresh(new_courseType)
        return new_courseType
    
    def update_courseType(self, id: int, courseType: CourseType) -> dict:        
        element = self.db.query(CourseTypeModel).filter(CourseTypeModel.id == id).first()                
        element.name = courseType.name
        element.number = courseType.number     
        self.db.commit()        
        self.db.refresh(element)        
        return element