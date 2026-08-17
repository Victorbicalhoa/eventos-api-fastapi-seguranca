from fastapi import FastAPI
from app.routes.eventos import router as eventos_router
from app.routes.pages import router as pages_router
    

app = FastAPI()
app.include_router(eventos_router)
app.include_router(pages_router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Eventos API!"}