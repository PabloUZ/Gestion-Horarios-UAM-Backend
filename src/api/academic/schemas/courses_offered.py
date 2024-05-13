from pydantic import BaseModel, Field, validator
from typing import Optional

class CoursesOffered(BaseModel):
    course_id: int = Field(gt=0, title="ID of the course")
    faculty_id: int = Field(gt=0, title="ID of the faculty")
    
    class Config:
        json_schema_extra = {
            "example": {
                "course_id": 1,
                "faculty_id": 1
            }
        }