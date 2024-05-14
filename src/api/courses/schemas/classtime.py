from pydantic import BaseModel, Field
from typing import Optional

class Classtime (BaseModel):
    id: Optional[int] = Field(default=None, title="Código del grupo")
    day: str = Field(default=None, title="Día que se ve dicha materia")
    start_hour: int = Field(title="Hora de inicio") 
    end_hour: int = Field(title="Hora final") 
    start_minute: int = Field(title="Minuto de inicio") 
    end_minute:int = Field(title="Minuto final") 
    group_id: int = Field(title="Id del grupo al que pertenece el horario")
    room_id: Optional[int] = Field(default=None, title="Salón en el que se dictará la materia")