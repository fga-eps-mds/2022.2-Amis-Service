import pytest 
from ..main import app
from httpx import AsyncClient

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
        GLOBAL_RESPONSE = response
    assert response.status_code == 201

# GET ALL
@pytest.mark.asyncio
async def test_read_all_recitas():
    '''Função para testar exibição de todas receitas'''
    async with AsyncClient(app = app, base_url = HTTPS_RECEITA) as async_client:
        response = await async_client.get("/receita/")
    assert response.status_code == 200

# GET BY ID
@pytest.mark.asyncio
async def test_read_by_id_receitas():
    '''Função para testar pesquisa de receitas por id'''
    async with AsyncClient(app = app,base_url = HTTPS_RECEITA) as async_client:
        response = await async_client.get(f"/receita/{id}")
    assert response.status_code == 200

# UPDATE BY ID
@pytest.mark.asyncio
async def test_update_by_id_receita():
    '''Função para testar modificação de objeto receita por ID'''
    data = {
        "nome": NOME_RECEITA,
        "ingredientes": INGREDIENTES,
        "modo_preparo": MODO_PREPARO
    }

    async with AsyncClient(app = app, base_url = HTTPS_RECEITA) as async_client:
        response = await async_client.put(f"/receita/{GLOBAL_RESPONSE.json()['id']}", json = data)
    assert response.status_code == 200

# DELETE POR ID
@pytest.mark.asyncio
async def test_delete_by_id_receitas():
    '''Função para testar apagar receita por ID'''
    async with AsyncClient(app = app, base_url = HTTPS_RECEITA) as async_client:
        response = await async_client.delete(f"/receita/{GLOBAL_RESPONSE.json()['id']}")
    assert response.status_code == 204