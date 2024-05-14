from typing import List
from src.api.academic.schemas.courses_offered import CoursesOffered
from src.api.academic.models.courses_offered import CourseOffered as CoursesOfferedModel

class CourseOfferedRepository():
    def __init__(self, db) -> None:
        self.db = db
        
    def get_courses_offered(self, offset:int , limit:int) -> List[CoursesOffered]:
        courses_offered = self.db.query(CoursesOfferedModel)
        if(offset is not None):
            courses_offered = courses_offered.offset(offset)
        if (limit is not None):
            courses_offered = courses_offered.limit(limit)
        return courses_offered.all()
    
    def get_course_offered(self, course_offered_id:str) -> CoursesOffered:
        course_offered = self.db.query(CoursesOfferedModel).filter(CoursesOfferedModel.id == course_offered_id).first()
        return course_offered
    
    def create_course_offered(self, course_offered:CoursesOffered) -> CoursesOffered:
        new_course_offered = CoursesOfferedModel(**course_offered.model_dump())
        self.db.add(new_course_offered)
        self.db.commit()
        self.db.refresh(new_course_offered)
        return new_course_offered
    
    def update_course_offered(self, course_offered_id:int) -> CoursesOffered:
        upd_course_offered = self.db.query(CoursesOfferedModel).filter(CoursesOfferedModel.id == course_offered_id).first()
        self.db.commit()
        self.db.refresh(upd_course_offered)
        return upd_course_offered
    
    def delete_course_offered(self, course_offered_id:int) -> dict:
        del_course_offered = self.db.query(CoursesOfferedModel).filter(CoursesOfferedModel.id == course_offered_id).first()
        self.db.delete(del_course_offered)
        self.db.commit()
        return del_course_offered