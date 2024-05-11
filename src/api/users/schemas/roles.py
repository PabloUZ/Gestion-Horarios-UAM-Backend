from pydantic import BaseModel, Field
from typing import Optional

class CreateRole(BaseModel):
    name: str = Field(min_length=3, max_length=50, pattern=r'^[A-Z]*$')
    description: Optional[str] = Field(min_length=5, max_length=50)
    active: bool = Field()

class UpdateRole(BaseModel):
    description: Optional[str] = Field(min_length=5, max_length=50)
    active: bool = Field()