from pydantic import BaseModel, Field, validator
from typing import Optional

class AcademicHistory(BaseModel):
    id: Optional[int] = Field(default= None, gt=0, title="ID of the faculty")
    created_at: Optional[str] = Field(default= None, title="Date and time of creation")
    study_plan_id: int = Field(gt=0, title="ID of the study plan")
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "created_at": "2021-01-01",
                "study_plan_id": 1
            }
        }
        