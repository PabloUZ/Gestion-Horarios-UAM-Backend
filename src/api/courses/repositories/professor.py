from typing import List
from src.api.courses.schemas.professor import Professor
from src.api.courses.models.professor import Professor as ProfessorModel
from sqlalchemy import func

class ProfessorRepository():    
    def __init__(self, db) -> None:        
        self.db = db
    
    def get_all_courses(self) -> List[Professor]: 
        query = self.db.query(ProfessorModel)
        return query.all()
    
    def get_professor_by_id(self, id: int ):
        element = self.db.query(ProfessorModel).filter(ProfessorModel.id == id).first()    
        return element

    def delete_professor(self, id: int ) -> dict: 
        element: Professor= self.db.query(ProfessorModel).filter(ProfessorModel.id == id).first()       
        self.db.delete(element)    
        self.db.commit()    
        return element

    def create_new_professor(self, professor:Professor ) -> dict:
        new_professor = ProfessorModel(**professor.model_dump())    
        self.db.add(new_professor)
        self.db.commit()    
        self.db.refresh(new_professor)
        return new_professor
    
    def update_professor(self, id: int, professor: Professor) -> dict:        
        element = self.db.query(ProfessorModel).filter(ProfessorModel.id == id).first()                
        element.name = professor.name      
        self.db.commit()        
        self.db.refresh(element)        
        return element