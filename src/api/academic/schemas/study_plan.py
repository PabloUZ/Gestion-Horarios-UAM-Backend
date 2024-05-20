from pydantic import BaseModel, Field, validator
from typing import Optional

class StudyPlan(BaseModel):
    id: Optional[int] = Field(default= None, gt=0, title="ID of the faculty")
    name: str = Field(title="Name of the faculty")
    year: Optional[int] = Field(title="Year of the study plan")
    program_id: int = Field(gt=0, title="ID of the program")
    
    @validator("year")
    def validate_year(cls, v):
        if v > 2024:
            raise ValueError("Year must be less than 2024")
        return v
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Study Plan 2021",
                "year": "2024",
                "program_id": 1
            }
        }
        
