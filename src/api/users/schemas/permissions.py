from pydantic import BaseModel, Field
from typing import Optional

class CreatePermission(BaseModel):
    name: str = Field(min_length=3, max_length=50, pattern=r'^[A-Z_]*$')
    description: Optional[str] = Field(min_length=5, max_length=50)

class UpdatePermission(BaseModel):
    description: Optional[str] = Field(min_length=5, max_length=50)