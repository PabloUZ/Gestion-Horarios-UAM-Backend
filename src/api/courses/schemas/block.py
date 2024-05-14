from pydantic import BaseModel, Field
from typing import Optional

class Block (BaseModel):
    id: Optional[int] = Field(default=None, title="Código del bloque")
    name: str = Field(min_length=4, max_length=50, title="Nombre del bloque")
    prefix: str = Field(max_length=5, title="Prefijo del bloque")

    