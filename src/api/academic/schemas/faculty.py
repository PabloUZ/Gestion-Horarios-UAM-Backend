from pydantic import BaseModel, Field, validator
from typing import Optional

class Faculty(BaseModel):
    id: Optional[int] = Field(default= None, gt=0, title="ID of the faculty")
    name: str = Field(title="Name of the faculty")
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Faculty of Engineering"
            }
        }
