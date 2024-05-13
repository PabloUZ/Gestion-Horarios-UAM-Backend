from pydantic import BaseModel, Field, validator
from typing import Optional

class CoursesApproved(BaseModel):
    course_id: int = Field(gt=0, title="ID of the course")
    academic_history_id: int = Field(gt=0, title="ID of the academic history")
    
    class Config:
        json_schema_extra = {
            "example": {
                "course_id": 1,
                "academic_history_id": 1
            }
        }