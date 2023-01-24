from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

# UTILIZAR PARA RODAR LOCALMENTE
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
from .assistentes.router import router as assistentes_router
from .alunas.router import router as aluna_router
from .turmas.router import router as turma_router
from .matricula.router import router as matricula_router

from .config import settings

app.include_router(aluna_router)
app.include_router(turma_router)
app.include_router(assistentes_router)
app.include_router(matricula_router)

@app.get('/')
async def hello_world():
    return {
        "db_type": settings.db_type,
        "db_url": settings.db_url,
    }