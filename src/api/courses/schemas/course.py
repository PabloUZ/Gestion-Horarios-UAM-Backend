from pydantic import BaseModel, Field
from typing import Optional

class Course (BaseModel):
    code: str = Field(min_length=0, max_length=8, title="Código de la materia")
    name: str = Field(min_length=1, max_length=100, title="Nombre de la materia")
    credits: Optional[int] = Field(default=None, title="Número de creditos de la materia")
    type_id: Optional[int] = Field(default=None, title="Tipo de materia")

