from typing import List
from src.api.academic.schemas.academic_history import AcademicHistory
from src.api.academic.models.academic_history import AcademicHistory as AcademicHistoryModel

class AcademicHistoryRepository():
    def __init__(self, db) -> None:
        self.db = db
        
    def get_academic_histories(self, offset:int , limit:int) -> List[AcademicHistory]:
        academic_histories = self.db.query(AcademicHistoryModel)
        if(offset is not None):
            academic_histories = academic_histories.offset(offset)
        if (limit is not None):
            academic_histories = academic_histories.limit(limit)
        return academic_histories.all()
    
    def get_academic_history(self, academic_history_id:int) -> AcademicHistory:
        academic_history = self.db.query(AcademicHistoryModel).filter(AcademicHistoryModel.id == academic_history_id).first()
        return academic_history
    
    def create_academic_history(self, academic_history:AcademicHistory) -> AcademicHistory:
        new_academic_history = AcademicHistoryModel(**academic_history.model_dump())
        self.db.add(new_academic_history)
        self.db.commit()
        self.db.refresh(new_academic_history)
        return new_academic_history
    
    def update_academic_history(self, academic_history_id:int, academic_history:AcademicHistory) -> AcademicHistory:
        upd_academic_history = self.db.query(AcademicHistoryModel).filter(AcademicHistoryModel.id == academic_history_id).first()
        upd_academic_history.created_at = academic_history.created_at
        upd_academic_history.study_plan_id = academic_history.study_plan_id
        upd_academic_history.user_cc = academic_history.user_cc
        self.db.commit()
        self.db.refresh(upd_academic_history)
        return upd_academic_history
    
    def delete_academic_history(self, academic_history_id:int) -> dict:
        del_academic_history = self.db.query(AcademicHistoryModel).filter(AcademicHistoryModel.id == academic_history_id).first()
        self.db.delete(del_academic_history)
        self.db.commit()
        return del_academic_history