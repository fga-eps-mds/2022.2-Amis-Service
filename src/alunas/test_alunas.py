import pytest
from main import app
from httpx import AsyncClient

nome = 'Maria das Dores de Souza'
nomeSocial = 'Mariela'
cpf = '50070792003'
rg = '2154992'
dataNascimento = '12/02/1970'
nomePai = 'Joao'
nomeMae = 'Joana'
deficiencia = False
idEndereco = 1

global_response = []

# CREATE
@pytest.mark.asyncio
async def test_create_aluna():
    data = {
        "nome": nome,
        "nomeSocial": nomeSocial,
        "cpf": cpf,
        "rg": rg,
        "dNascimento": dataNascimento,
        "nomePai": nomePai,
        "nomeMae": nomeMae,
        "deficiencia": deficiencia,
        "idEndereco": idEndereco
    }
    async with AsyncClient(app=app, base_url="http://alunas") as ac:
        response = await ac.post("/alunas/", json=data) 
        global global_response 
        global_response = response
    assert response.status_code == 201 

# GET ALL
@pytest.mark.asyncio
async def test_read_all_alunas():
    async with AsyncClient(app=app, base_url="http://alunas") as ac:
        response = await ac.get("/alunas/")
    assert response.status_code == 200

# GET BY CPF
@pytest.mark.asyncio
async def test_read_by_cpf_alunas():
    async with AsyncClient(app=app, base_url="http://alunas") as ac:
        response = await ac.get(f"/alunas/{cpf}")
    assert response.status_code == 200
        
# @pytest.mark.asyncio
# async def test_update_by_cpf_aluna():
#     data = {
#         "nome": nome,
#         "cpf": '1',
#         "turma": '130',
#         "idade": 42
#     }
#     async with AsyncClient(app=app, base_url="http://alunas") as ac:
#         response = await ac.put("/alunas/1", json=data)
#     assert response.status_code == 201

# UPDATE BY ID
@pytest.mark.asyncio
async def test_update_by_id_aluna():

    data = {
        "nome": nome,
        "nomeSocial": 'Felipe',
        "cpf": cpf,
        "rg": rg,
        "dNascimento": '00/00/00',
        "nomePai": nomePai,
        "nomeMae": nomeMae,
        "deficiencia": deficiencia,
        "idEndereco": idEndereco
    }

    async with AsyncClient(app=app, base_url="http://alunas") as ac:
        response = await ac.put(f"/alunas/{global_response.json()['id']}", json=data)
    assert response.status_code == 200

# DELETE BY CPF
@pytest.mark.asyncio
async def test_delete_by_id_alunas():
    async with AsyncClient(app=app, base_url="http://alunas") as ac:
        response = await ac.delete(f"/alunas/{global_response.json()['id']}")
    assert response.status_code == 204 
