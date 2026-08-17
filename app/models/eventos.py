from pydantic import BaseModel
from datetime import date

class EventoCreate(BaseModel):
    name: str
    data: date
    organizador: str

class EventoPublico(BaseModel):
    id: int
    name: str
    data: date
    organizador: str

class EventoInterno(BaseModel):
    id: int
    name: str
    data: date
    organizador: str
    organizador_id: int
    token_auditoria: str 

    