import pytest
from main import app
from httpx import AsyncClient

DESCRICAO = 'Turma biscoito 101'
TURNO = '1'
CAPACIDADE = 20
HORARIO_INICIO = '14:00'
HORARIO_FIM = '16:00'
DATA_INICIO = '12/02/2023'
DATA_FIM = '12/03/2023'

GLOBAL_RESPONSE = []
HTTPS_TURMAS = "https://turmas"

# CREATE
@pytest.mark.asyncio
async def test_create_turma():
    '''Função para testar a criação de uma turma'''
    data = {
        "descricao": DESCRICAO,
        "turno": TURNO,
        "capacidade": CAPACIDADE,
        "horarioInicio": HORARIO_INICIO,
        "horarioFim": HORARIO_FIM,
        "dataInicio": DATA_INICIO,
        "dataFim": DATA_FIM
    }
    async with AsyncClient(app = app, base_url = HTTPS_TURMAS) as async_client:
        response = await async_client.post("/turmas/", json=data)
        global GLOBAL_RESPONSE
        GLOBAL_RESPONSE = response
    assert response.status_code == 201

# GET ALL
@pytest.mark.asyncio
async def test_read_all_turmas():
    '''Função para testar exibição de todas turmas (ainda sem paginação)'''
    async with AsyncClient(app = app, base_url = HTTPS_TURMAS) as async_client:
        response = await async_client.get("/turmas/")
    assert response.status_code == 200

# GET BY CAPACIDADE
@pytest.mark.asyncio
async def test_read_by_cpf_turmas():
    '''Função para testar pesquisa de turma por CAPACIDADE'''
    async with AsyncClient(app = app, base_url = HTTPS_TURMAS) as async_client:
        response = await async_client.get(f"/turmas/{CAPACIDADE}")
    assert response.status_code == 200

# UPDATE BY ID
@pytest.mark.asyncio
async def test_update_by_id_turma():
    '''Função para testar modificação de objeto turma por ID'''
    data = {
        "descricao": DESCRICAO,
        "turno": 'Felipe',
        "capacidade": CAPACIDADE,
        "rg": HORARIO_INICIO,
        "horarioFim": '00/00/00',
        "dataInicio": DATA_INICIO,
        "dataFim": DATA_FIM
    }

    async with AsyncClient(app = app, base_url = HTTPS_TURMAS) as async_client:
        response = await async_client.put(f"/turmas/{GLOBAL_RESPONSE.json()['id']}", json = data)
    assert response.status_code == 200

# DELETE BY CAPACIDADE
@pytest.mark.asyncio
async def test_delete_by_id_turmas():
    '''Função para testar apagar turma por ID'''
    async with AsyncClient(app = app, base_url = HTTPS_TURMAS) as async_client:
        response = await async_client.delete(f"/turmas/{GLOBAL_RESPONSE.json()['id']}")
    assert response.status_code == 204
