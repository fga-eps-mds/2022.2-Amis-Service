import pytest
from ..main import app, test
from httpx import AsyncClient

GLOBAL_RESPONSE_ALUNA = []
GLOBAL_RESPONSE_TURMA = []
GLOBAL_RESPONSE = []

HTTPS_MATRICULA = "https://matricula"
HTTPS_ALUNAS = "https://alunas"
HTTPS_TURMAS = "https://turmas"

# ALUNA 1
NOME = 'Maria das Dores de Souza'
NOME_SOCIAL = 'Mariela'
CPF = '50070792003'
RG = '2154992'
DATA_NASC = '12/02/1970'
NOME_PAI = 'Joao'
NOME_MAE = 'Joana'
DEFICIENCIA = False
ENDERECO_ID = 1

# CREATE ALUNA 1
@pytest.mark.asyncio
async def test_create_aluna():
    '''Função para testar a criação de uma aluna'''
    data = {
        "nome": NOME,
        "nomeSocial": NOME_SOCIAL,
        "cpf": CPF,
        "rg": RG,
        "dNascimento": DATA_NASC,
        "nomePai": NOME_PAI,
        "nomeMae": NOME_MAE,
        "deficiencia": DEFICIENCIA,
        "idEndereco": ENDERECO_ID
    }
    async with AsyncClient(app = app, base_url = HTTPS_ALUNAS) as async_client:
        TOKEN = await test()
        headers = {"Authorization": "Bearer " + TOKEN}
        responseAluna = await async_client.post("/alunas/", json=data, headers=headers)
        global GLOBAL_RESPONSE_ALUNA
        GLOBAL_RESPONSE_ALUNA = responseAluna
    assert responseAluna.status_code == 201

# TURMA
DESCRICAO = 'Turma da Maria'
TURNO = '1'
CAPACIDADE = 20
HORARIO_INICIO = '14:00'
HORARIO_FIM = '16:00'
DATA_INICIO = '12/02/2023'
DATA_FIM = '12/03/2023'

# CREATE TURMA
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
        TOKEN = await test()
        headers = {"Authorization": "Bearer " + TOKEN}
        responseTurma = await async_client.post("/turmas/", json=data, headers=headers)
        global GLOBAL_RESPONSE_TURMA
        GLOBAL_RESPONSE_TURMA = responseTurma
    assert responseTurma.status_code == 201

# MATRICULA
ID_TURMA = 1
ID_ALUNA = "1"

# CREATE MATRICULA
@pytest.mark.asyncio
async def test_create_matricula():
    '''Função para testar a criação de uma matricula'''
    data = {
        "idTurma": ID_TURMA,
        "idAluna": ID_ALUNA,
    }
    async with AsyncClient(app = app, base_url = HTTPS_MATRICULA) as async_client:
        TOKEN = await test()
        headers = {"Authorization": "Bearer " + TOKEN}
        response = await async_client.post("/matricula/", json=data, headers=headers)
        global GLOBAL_RESPONSE
        GLOBAL_RESPONSE = response
    assert response.status_code == 201

# GET ALL
@pytest.mark.asyncio
async def test_read_all_matriculas():
    '''Função para testar exibição de todas matriculas (ainda sem paginação)'''
    async with AsyncClient(app = app, base_url = HTTPS_MATRICULA) as async_client:
        TOKEN = await test()
        headers = {"Authorization": "Bearer " + TOKEN}
        response = await async_client.get("/matricula/", headers=headers)
    assert response.status_code == 200

# GET BY ID
@pytest.mark.asyncio
async def test_read_by_id_matricula():
    '''Função para testar pesquisa de matricula por ID'''
    async with AsyncClient(app = app, base_url = HTTPS_MATRICULA) as async_client:
        TOKEN = await test()
        headers = {"Authorization": "Bearer " + TOKEN}
        response = await async_client.get(f"/matricula/{ID_TURMA}", headers=headers)
    assert response.status_code == 200

# DELETE BY ID
@pytest.mark.asyncio
async def test_delete_by_id_matricula():
    '''Função para testar apagar matricula por ID da turma e aluna'''
    async with AsyncClient(app = app, base_url = HTTPS_MATRICULA) as async_client:
        TOKEN = await test()
        headers = {"Authorization": "Bearer " + TOKEN}
        response = await async_client.delete(f"/matricula/{ID_TURMA}/{ID_ALUNA}", headers=headers)
    assert response.status_code == 204

# GET VAGAS BY ID
@pytest.mark.asyncio
async def test_read_by_id_matricula():
    '''Função para testar pesquisa de vagas da turma por ID'''
    async with AsyncClient(app = app, base_url = HTTPS_MATRICULA) as async_client:
        TOKEN = await test()
        headers = {"Authorization": "Bearer " + TOKEN}
        response = await async_client.get(f"/matricula/turma/{ID_TURMA}", headers=headers)
    assert response.status_code == 200