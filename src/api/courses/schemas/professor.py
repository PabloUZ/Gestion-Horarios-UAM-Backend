from pydantic import BaseModel, Field
from typing import Optional

class Professor (BaseModel):
    id: Optional[int] = Field(default=None, title="Código del profesor")
    name: str = Field(min_length=4, max_length=50, title="Nombre del profesor")