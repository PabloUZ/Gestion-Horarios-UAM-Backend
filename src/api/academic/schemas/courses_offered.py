from pydantic import BaseModel, Field, validator
from typing import Optional

class CoursesOffered(BaseModel):
    id: Optional[int] = Field(default= None, gt=0, title="ID of the Course Offered")
    course_id: str = Field(title="ID of the course")
    study_plan_id: int = Field(gt=0, title="ID of the faculty")
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "course_id": "1",
                "study_plan_id": 1
            }
        }