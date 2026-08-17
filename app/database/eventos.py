from datetime import date, datetime

from app.models.eventos import EventoInterno

_eventos  = [
    EventoInterno(id=1, name="Evento 1", data=datetime.now().date(), organizador="Organizador Padrão", organizador_id=1, token_auditoria="token1"),
    EventoInterno(id=2, name="Evento 2", data=datetime.now().date(), organizador="Organizador Padrão", organizador_id=2, token_auditoria="token2")
]

def listar_eventos():
    return _eventos

def buscar_evento_por_id(evento_id: int):
    for evento in _eventos:
        if evento.id == evento_id:
            return evento
    return None

def criar_evento(name: str, data: date, organizador: str):
    novo_id = len(_eventos) + 1
    novo_evento = EventoInterno(
        id=novo_id,
        name=name,
        data=data,
        organizador= organizador,
        organizador_id=1,
        token_auditoria=f"audit-demo-{novo_id}"
    )
    _eventos.append(novo_evento)
    return novo_evento