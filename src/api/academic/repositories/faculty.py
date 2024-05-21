from typing import List
from src.api.academic.schemas.faculty import Faculty
from src.api.academic.models.faculty import Faculty as FacultyModel

class FacultyRepository():
    def __init__(self, db) -> None:
        self.db = db
        
    def get_faculties(self, offset:int , limit:int) -> List[Faculty]:
        faculties = self.db.query(FacultyModel)
        if(offset is not None):
            faculties = faculties.offset(offset)
        if (limit is not None):
            faculties = faculties.limit(limit)
        return faculties.all()
    
    def get_faculty(self, faculty_id:int) -> Faculty:
        faculty = self.db.query(FacultyModel).filter(FacultyModel.id == faculty_id).first()
        return faculty
    
    def create_faculty(self, faculty:Faculty) -> Faculty:
        new_faculty = FacultyModel(**faculty.model_dump())
        self.db.add(new_faculty)
        self.db.commit()
        self.db.refresh(new_faculty)
        print(new_faculty)
        return new_faculty
    
    def update_faculty(self, faculty_id:int, faculty:Faculty) -> Faculty:
        upd_faculty = self.db.query(FacultyModel).filter(FacultyModel.id == faculty_id).first()
        upd_faculty.name = faculty.name
        self.db.commit()
        self.db.refresh(upd_faculty)
        return upd_faculty
    
    def delete_faculty(self, faculty_id:int) -> dict:
        del_faculty = self.db.query(FacultyModel).filter(FacultyModel.id == faculty_id).first()
        self.db.delete(del_faculty)
        self.db.commit()
        return del_faculty