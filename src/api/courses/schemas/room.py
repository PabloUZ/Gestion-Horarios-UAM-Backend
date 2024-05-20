from pydantic import BaseModel, Field
from typing import Optional

class Room (BaseModel):
    id: Optional[int] = Field(default=None, title="Código del salón")
    name: str = Field(min_length=4, max_length=50, title="Nombre del salón")
    block_id: Optional[int] = Field(default=None, title="Bloque en dónde está el salón")

    