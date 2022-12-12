from fastapi import FastAPI, status
app = FastAPI()

# Routers
from .alunas.router import router as aluna_router

from config import settings

app = FastAPI()

app.include_router(aluna_router)

@app.get('/')
async def hello_world():
    return {
        "db_type": settings.db_type,
        "db_url": settings.db_url,
    }