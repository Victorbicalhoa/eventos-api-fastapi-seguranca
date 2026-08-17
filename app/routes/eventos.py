from fastapi import APIRouter, HTTPException
from app.models.eventos import EventoCreate, EventoPublico
from app.database import eventos as eventos_db

router = APIRouter()

@router.get("/eventos", response_model=list[EventoPublico])
async def read_eventos():
    return eventos_db.listar_eventos()


@router.get("/eventos/{evento_id}", response_model=EventoPublico)
async def read_evento(evento_id: int):
    evento = eventos_db.buscar_evento_por_id(evento_id)

    if evento is None:
        raise HTTPException(status_code=404, detail="Evento not found")
    
    return evento

@router.post("/eventos", status_code=201, response_model=EventoPublico)
async def create_evento(evento: EventoCreate):
    return eventos_db.criar_evento(
        name=evento.name,
        data=evento.data,
        organizador=evento.organizador
    )

@router.post("/eventos/sem-response-model", status_code=201)
async def create_evento_sem_response_model(evento: EventoCreate):   
    return eventos_db.criar_evento(
        name=evento.name,
        data=evento.data,
        organizador=evento.organizador
    )