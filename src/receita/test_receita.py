import pytest 
from ..main import app
from httpx import AsyncClient
from .repository import ReceitasRepository
from ..database import engine, Base, get_db
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

NOME_RECEITA = 'Bolo de cenoura'
INGREDIENTES = 'Farinha'
MODO_PREPARO = 'Assar no forno por 30 minutos'

GLOBAL_RESPONSE = []
HTTPS_RECEITA = "https://receita"

# CREATE
@pytest.mark.asyncio
async def test_create_receita():
    '''Função para testar a criação de uma receita'''
data = {
    "nome": NOME_RECEITA,
    "ingredientes": INGREDIENTES,
    "modo_preparo": MODO_PREPARO
}
async with AsyncClient( app = app, base_url = HTTPS_RECEITA) as async_client:
    response = await async_client.post("/receita/", json=data)
    global GLOBAL_RESPONSE
    GLOBAL_RESPONSE= response
assert response.status_code == 201

# GET ALL
@pytest.mark.asyncio
async def test_read_all_alunas():
    '''Função para testar exibição de todas receitas'''
    async with AsyncClient(app = app, base_url = HTTPS_RECEITA) as async_client:
        response = await async_client.get("/alunas/")
    assert response.status_code == 200