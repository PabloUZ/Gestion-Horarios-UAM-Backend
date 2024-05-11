from typing import List
from src.api.academic.schemas.study_plan import StudyPlan
from src.api.academic.models.study_plan import StudyPlan as StudyPlanModel

class StudyPlanRepository():
    def __init__(self, db) -> None:
        self.db = db
        
    def get_study_plans(self, offset:int , limit:int) -> List[StudyPlan]:
        study_plans = self.db.query(StudyPlanModel)
        if(offset is not None):
            study_plans = study_plans.offset(offset)
        if (limit is not None):
            study_plans = study_plans.limit(limit)
        return study_plans.all()
    
    def get_study_plan(self, study_plan_id:int) -> StudyPlan:
        study_plan = self.db.query(StudyPlanModel).filter(StudyPlanModel.id == study_plan_id).first()
        return study_plan
    
    def create_study_plan(self, study_plan:StudyPlan) -> StudyPlan:
        new_study_plan = StudyPlanModel(**study_plan.model_dump())
        self.db.add(new_study_plan)
        self.db.commit()
        self.db.refresh(new_study_plan)
        return new_study_plan
    
    def update_study_plan(self, study_plan_id:int, study_plan:StudyPlan) -> StudyPlan:
        upd_study_plan = self.db.query(StudyPlanModel).filter(StudyPlanModel.id == study_plan_id).first()
        upd_study_plan.name = study_plan.name
        upd_study_plan.year = study_plan.year
        upd_study_plan.program_id = study_plan.program_id
        self.db.commit()
        self.db.refresh(upd_study_plan)
        return upd_study_plan
    
    def delete_study_plan(self, study_plan_id:int) -> dict:
        del_study_plan = self.db.query(StudyPlanModel).filter(StudyPlanModel.id == study_plan_id).first()
        self.db.delete(del_study_plan)
        self.db.commit()
        return del_study_plan