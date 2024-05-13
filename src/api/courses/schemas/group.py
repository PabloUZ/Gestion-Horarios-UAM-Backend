from pydantic import BaseModel, Field
from typing import Optional

class Group (BaseModel):
    id: Optional[int] = Field(default=None, title="Código del grupo")
    name: str = Field(min_length=1, max_length=100, title="Nombre del grupo")
    number: int = Field(title='Número del grupo')
    course_code: str = Field(max_length=8, title="Código de la materia al que pertenece el grupo")
    proffesor_id: Optional[int] = Field(default=None, title="Profesor que dicta ese grupo")