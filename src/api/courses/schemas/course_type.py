from pydantic import BaseModel, Field
from typing import Optional

class CourseType (BaseModel):
    id: Optional[int] = Field(default=None, title="Código del grupo")
    name: str = Field(min_length=4, max_length=50, title="Nombre de la materia")