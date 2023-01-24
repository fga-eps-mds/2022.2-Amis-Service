from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
from alunas.router import router as aluna_router
#from turmas.router import router as turma_router

from config import settings

app = FastAPI()

app.include_router(aluna_router)
#app.include_router(turma_router)

@app.get('/')
async def hello_world():
    return {
        "db_type": settings.db_type,
        "db_url": settings.db_url,
    }