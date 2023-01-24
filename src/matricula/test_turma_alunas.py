import pytest
from ..main import app
from httpx import AsyncClient

ID_TURMA = 4
ID_ALUNAS = '1, 2, 3'

GLOBAL_RESPONSE = []
HTTPS_MATRICULA = "https://matricula"

# CREATE
@pytest.mark.asyncio
async def test_create_matricula():
    '''Função para testar a criação de uma matricula'''
    data = {
        "idTurma": ID_TURMA,
        "idAluna": ID_ALUNAS,
    }
    async with AsyncClient(app = app, base_url = HTTPS_MATRICULA) as async_client:
        response = await async_client.post("/matricula/", json=data)
        global GLOBAL_RESPONSE
        GLOBAL_RESPONSE = response
    assert response.status_code == 201

# GET ALL
@pytest.mark.asyncio
async def test_read_all_matriculas():
    '''Função para testar exibição de todas matriculas (ainda sem paginação)'''
    async with AsyncClient(app = app, base_url = HTTPS_MATRICULA) as async_client:
        response = await async_client.get("/matricula/")
    assert response.status_code == 200

# GET BY ID
@pytest.mark.asyncio
async def test_read_by_id_matricula():
    '''Função para testar pesquisa de matricula por ID'''
    async with AsyncClient(app = app, base_url = HTTPS_MATRICULA) as async_client:
        response = await async_client.get(f"/matricula/{ID_TURMA}")
    assert response.status_code == 200

# DELETE BY ID
@pytest.mark.asyncio
async def test_delete_by_id_matricula():
    '''Função para testar apagar matricula por ID da turma e aluna'''
    async with AsyncClient(app = app, base_url = HTTPS_MATRICULA) as async_client:
        response = await async_client.delete(f"/matricula/{ID_TURMA}/{ID_ALUNAS}")
    assert response.status_code == 204

# GET VAGAS BY ID
@pytest.mark.asyncio
async def test_read_by_id_matricula():
    '''Função para testar pesquisa de vagas da turma por ID'''
    async with AsyncClient(app = app, base_url = HTTPS_MATRICULA) as async_client:
        response = await async_client.get(f"/matricula/turma/{ID_TURMA}")
    assert response.status_code == 200