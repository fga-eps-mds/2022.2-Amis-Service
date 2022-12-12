from sqlalchemy.orm import Session
from ..database import engine, Base, get_db as get_database
from fastapi import APIRouter, status, HTTPException, Response, Depends
from .model import Alunas
from .repository import AlunasRepository
from .schema import AlunasRequest, AlunasResponse

Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix = '/alunas',
    tags = ['alunas'],
    responses = {404: {"description": "Not found"}},
)

@router.post("/",
    response_model = AlunasResponse,
    status_code = status.HTTP_201_CREATED
)
def create(request: AlunasRequest, database: Session = Depends(get_database)):
    '''Cria e salva um objeto aluna por meio do método POST'''
    alunas = AlunasRepository.save(database, Alunas(**request.dict()))
    return alunas


# GET ALL
@router.get("/", response_model = list[AlunasResponse])
def find_all(database: Session = Depends(get_database)):
    '''Faz uma query de todos os objetos aluna na DB (sem paginação)'''
    alunas = AlunasRepository.find_all(database)
    print(alunas)
    return [AlunasResponse.from_orm(aluna) for aluna in alunas]


# READ BY cpf
@router.get("/{cpf}", response_model = AlunasResponse)
def find_by_cpf(cpf: str, database: Session = Depends(get_database)):
    '''Dado o CPF como parâmetro, encontra a aluna com esse CPF'''
    aluna = AlunasRepository.find_by_cpf(database, cpf)
    if not aluna:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail = "aluna não encontrada"
        )
    return AlunasResponse.from_orm(aluna)

# DELETE BY id
@router.delete("/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_by_id(id: str, database: Session = Depends(get_database)):
    '''Dado o ID da aluna, deleta o objeto da DB por meio do método DELETE'''
    if not AlunasRepository.exists_by_id(database, id):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, detail="aluna não encontrada"
        )
    AlunasRepository.delete_by_id(database, id)
    return Response(status_code = status.HTTP_204_NO_CONTENT)

# UPDATE BY ID
@router.put("/{id}", response_model = AlunasResponse)
def update(id: str, request: AlunasRequest, database: Session = Depends(get_database)):
    '''Dado o ID da aluna, atualiza os dados cadastrais na DB por meio do método PUT'''
    if not AlunasRepository.exists_by_id(database, id):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, detail = "Aluna não encontrada"
        )
    aluna = AlunasRepository.save(database, Alunas(id = id, **request.dict()))
    return AlunasResponse.from_orm(aluna)