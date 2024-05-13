from typing import List
from src.api.academic.schemas.courses_approved import CoursesApproved
from src.api.academic.models.courses_approved import CourseApproved as CoursesApprovedModel

class CourseApprovedRepository():
    def __init__(self, db) -> None:
        self.db = db
        
    def get_courses_approved(self, offset:int , limit:int) -> List[CoursesApproved]:
        courses_approved = self.db.query(CoursesApprovedModel)
        if(offset is not None):
            courses_approved = courses_approved.offset(offset)
        if (limit is not None):
            courses_approved = courses_approved.limit(limit)
        return courses_approved.all()
    
    def get_course_approved(self, course_id:int, academic_history_id:int) -> CoursesApproved:
        course_approved = self.db.query(CoursesApprovedModel).filter(CoursesApprovedModel.course_id == course_id, CoursesApprovedModel.academic_history_id == academic_history_id).first()
        return course_approved
    
    def create_course_approved(self, course_approved:CoursesApproved) -> CoursesApproved:
        new_course_approved = CoursesApprovedModel(**course_approved.model_dump())
        self.db.add(new_course_approved)
        self.db.commit()
        self.db.refresh(new_course_approved)
        return new_course_approved
    
    def update_course_approved(self, course_id:int, academic_history_id:int, course_approved:CoursesApproved) -> CoursesApproved:
        upd_course_approved = self.db.query(CoursesApprovedModel).filter(CoursesApprovedModel.course_id == course_id, CoursesApprovedModel.academic_history_id == academic_history_id).first()
        self.db.commit()
        self.db.refresh(upd_course_approved)
        return upd_course_approved
    
    def delete_course_approved(self, course_id:int, academic_history_id:int) -> dict:
        del_course_approved = self.db.query(CoursesApprovedModel).filter(CoursesApprovedModel.course_id == course_id, CoursesApprovedModel.academic_history_id == academic_history_id).first()
        self.db.delete(del_course_approved)
        self.db.commit()
        return del_course_approved