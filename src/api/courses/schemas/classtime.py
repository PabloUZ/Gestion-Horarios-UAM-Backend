from pydantic import BaseModel, Field
from typing import Optional

class Classtime (BaseModel):
    id: Optional[int] = Field(default=None, title="Código del grupo")
    day: str = Field(default=None, title="Día que se ve dicha materia")
    start_hour: str = Field(min_length=4, max_length=50, title="Hora de inicio") 
    end_hour:str = Field(min_length=4, max_length=50, title="Hora final") 
    start_minute: str = Field(min_length=4, max_length=50, title="Minuto de inicio") 
    end_minute:str = Field(min_length=4, max_length=50, title="Minuto final") 