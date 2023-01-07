import pytest
from ..main import app
from httpx import AsyncClient

NOME = 'Maria das Dores de Souza'
NOME_SOCIAL = 'Mariela'
CPF = '50070792003'
RG = '2154992'
DATA_NASC = '12/02/1970'
NOME_PAI = 'Joao'
NOME_MAE = 'Joana'
DEFICIENCIA = False
ENDERECO_ID = 1

GLOBAL_RESPONSE = []
HTTPS_ASSISTENTE = "https://assistentes"

# CREATE
@pytest.mark.asyncio
async def test_create_assistente():
    '''Função para testar a criação de uma assistente'''
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
    async with AsyncClient(app = app, base_url = HTTPS_ASSISTENTE) as async_client:
        response = await async_client.post("/assistentes/", json=data)
        global GLOBAL_RESPONSE
        GLOBAL_RESPONSE = response
    assert response.status_code == 201

# GET ALL
@pytest.mark.asyncio
async def test_read_all_assistente():
    '''Função para testar exibição de todas assistentes (ainda sem paginação)'''
    async with AsyncClient(app = app, base_url = HTTPS_ASSISTENTE) as async_client:
        response = await async_client.get("/assistentes/")
    assert response.status_code == 200

# GET BY CPF
@pytest.mark.asyncio
async def test_read_by_cpf_assistentes():
    '''Função para testar pesquisa de assistente por CPF'''
    async with AsyncClient(app = app, base_url = HTTPS_ASSISTENTE) as async_client:
        response = await async_client.get(f"/assistentes/{CPF}")
    assert response.status_code == 200

# UPDATE BY ID
@pytest.mark.asyncio
async def test_update_by_id_assistente():
    '''Função para testar modificação de objeto assistente por ID'''
    data = {
        "nome": NOME,
        "nomeSocial": 'Felipe',
        "cpf": CPF,
        "rg": RG,
        "dNascimento": '00/00/00',
        "nomePai": NOME_PAI,
        "nomeMae": NOME_MAE,
        "deficiencia": DEFICIENCIA,
        "idEndereco": ENDERECO_ID
    }

    async with AsyncClient(app = app, base_url = HTTPS_ASSISTENTE) as async_client:
        response = await async_client.put(f"/assistentes/{GLOBAL_RESPONSE.json()['id']}", json = data)
    assert response.status_code == 200

# DELETE BY ID
@pytest.mark.asyncio
async def test_delete_by_id_assistente():
    '''Função para testar apagar assistente por ID'''
    async with AsyncClient(app = app, base_url = HTTPS_ASSISTENTE) as async_client:
        response = await async_client.delete(f"/assistente/{GLOBAL_RESPONSE.json()['id']}")
    assert response.status_code == 204
