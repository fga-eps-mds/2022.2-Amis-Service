from sqlalchemy.orm import Session
from ..database import engine, Base, get_db as get_database
from fastapi import APIRouter, status, HTTPException, Response, Depends
from ..model.model import Assistentes
from .repository import AssistentesRepository
from .schema import AssistentesRequest, AssistentesResponse
from ..security import get_password_hash

Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix = '/assistentes',
    tags = ['assistentes'],
    responses = {404: {"description": "Not found"}},
)

@router.post("/",
    response_model = AssistentesResponse,
    status_code = status.HTTP_201_CREATED
)
def create(request: AssistentesRequest, database: Session = Depends(get_database)):
    '''Cria e salva um objeto assistente por meio do método POST'''
    assistenteRequisicao = Assistentes(**request.dict())
    assistenteRequisicao.senha = get_password_hash(assistenteRequisicao.senha)
    assistentes = AssistentesRepository.save(database, assistenteRequisicao)
    return assistentes


# GET ALL
@router.get("/", response_model = list[AssistentesResponse])
def find_all(database: Session = Depends(get_database)):
    '''Faz uma query de todos os objetos assistente na DB (sem paginação)'''
    assistentes = AssistentesRepository.find_all(database)
    print(assistentes)
    return [AssistentesResponse.from_orm(assistente) for assistente in assistentes]


# READ BY cpf
@router.get("/{cpf}", response_model = AssistentesResponse)
def find_by_cpf(cpf: str, database: Session = Depends(get_database)):
    '''Dado o CPF como parâmetro, encontra a assistente com esse CPF'''
    assistente = AssistentesRepository.find_by_cpf(database, cpf)
    if not assistente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail = "Assistente não encontrada"
        )
    return AssistentesResponse.from_orm(assistente)

# DELETE BY id
@router.delete("/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_by_id(id: str, database: Session = Depends(get_database)):
    '''Dado o ID da assistente, deleta o objeto da DB por meio do método DELETE'''
    if not AssistentesRepository.exists_by_id(database, id):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, detail="Assistente não encontrada"
        )
    AssistentesRepository.delete_by_id(database, id)
    return Response(status_code = status.HTTP_204_NO_CONTENT)

# UPDATE BY ID
@router.put("/{id}", response_model = AssistentesResponse)
def update(id: str, request: AssistentesRequest, database: Session = Depends(get_database)):
    '''Dado o ID da assistente, atualiza os dados cadastrais na DB por meio do método PUT'''
    if not AssistentesRepository.exists_by_id(database, id):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, detail = "Assistente não encontrada"
        )
    assistente = AssistentesRepository.save(database, Assistentes(id = id, **request.dict()))
    return AssistentesResponse.from_orm(assistente)