from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.database import eventos as eventos_db


router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/painel/eventos", response_class=HTMLResponse)
async def eventos_page(request: Request):
    eventos = eventos_db.listar_eventos()

    return templates.TemplateResponse(
        request=request,
        name="eventos.html",
        context={"eventos": eventos}
    )

@router.get("/painel/eventos/{evento_id}", response_class=HTMLResponse)
async def evento_detail_page(request: Request, evento_id: int):
    evento = eventos_db.buscar_evento_por_id(evento_id)

    if evento is None:
        return templates.TemplateResponse(
            request=request,
            name="404.html",
            context={"request": request},
            status_code=404
        )

    return templates.TemplateResponse(
        request=request,
        name="evento_detalhes.html",
        context={"evento": evento}
    )