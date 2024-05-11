from pydantic import BaseModel, Field
from typing import Optional

class Group (BaseModel):
    id: Optional[int] = Field(default=None, title="Código del grupo")
    name: str = Field(min_length=4, max_length=50, title="Nombre del grupo")