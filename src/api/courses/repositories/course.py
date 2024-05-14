from typing import List
from src.api.courses.schemas.course import Course
from src.api.courses.models.course import Course as CourseModel
from sqlalchemy import func

class CourseRepository():    
    def __init__(self, db) -> None:        
        self.db = db
    
    def get_all_courses(self) -> List[Course]: 
        query = self.db.query(CourseModel)
        return query.all()
    
    def get_course_by_code(self, code: str):
        element = self.db.query(CourseModel).filter(CourseModel.code == code).first()    
        return element

    def delete_course(self, id: int ) -> dict: 
        element: Course= self.db.query(CourseModel).filter(CourseModel.id == id).first()       
        self.db.delete(element)    
        self.db.commit()    
        return element

    def create_new_course(self, course:Course ) -> dict:
        new_course = CourseModel(**course.model_dump())    
        self.db.add(new_course)
        self.db.commit()    
        self.db.refresh(new_course)
        return new_course
    
    def update_course(self, id: int, course: Course) -> dict:        
        element = self.db.query(CourseModel).filter(CourseModel.id == id).first()                
        element.name = course.name
        element.credits = course.credits
        element.type = course.type        
        self.db.commit()        
        self.db.refresh(element)        
        return element
