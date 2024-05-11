from pydantic import BaseModel, Field
from typing import Optional

class Course (BaseModel):
    code: Optional[int] = Field(default=None, title="Código de la materia")
    name: str = Field(min_length=4, max_length=50, title="Nombre de la materia")
    credits: int = Field(title="Número de creditos de la materia")
    type: str = Field(min_length=4, max_length=50, title="Tipo de materia")

