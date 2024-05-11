from typing import List
from src.api.academic.schemas.program import Program
from src.api.academic.models.program import Program as ProgramModel

class ProgramRepository():
    def __init__(self, db) -> None:
        self.db = db
        
    def get_programs(self, offset:int , limit:int) -> List[Program]:
        programs = self.db.query(ProgramModel)
        if(offset is not None):
            programs = programs.offset(offset)
        if (limit is not None):
            programs = programs.limit(limit)
        return programs.all()
    
    def get_program(self, program_id:int) -> Program:
        program = self.db.query(ProgramModel).filter(ProgramModel.id == program_id).first()
        return program
    
    def create_program(self, program:Program) -> Program:
        new_program = ProgramModel(**program.model_dump())
        self.db.add(new_program)
        self.db.commit()
        self.db.refresh(new_program)
        return new_program
    
    def update_program(self, program_id:int, program:Program) -> Program:
        upd_program = self.db.query(ProgramModel).filter(ProgramModel.id == program_id).first()
        upd_program.name = program.name
        upd_program.faculty_id = program.faculty_id
        self.db.commit()
        self.db.refresh(upd_program)
        return upd_program
    
    def delete_program(self, program_id:int) -> dict:
        del_program = self.db.query(ProgramModel).filter(ProgramModel.id == program_id).first()
        self.db.delete(del_program)
        self.db.commit()
        return del_program