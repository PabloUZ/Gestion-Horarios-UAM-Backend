from pydantic import BaseModel, Field, validator
from typing import Optional

class CoursesApproved(BaseModel):
    id: Optional[int] = Field(default= None, gt=0, title="ID of the Course Approved")
    course_id: str = Field(title="ID of the course")
    academic_history_id: int = Field(gt=0, title="ID of the academic history")
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "course_id": "1",
                "academic_history_id": 1
            }
        }