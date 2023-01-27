from sqlalchemy.orm import Session
from ..database import engine, Base, get_db as get_database
from fastapi import APIRouter, status, HTTPException, Response, Depends
# from .model import Turmas
from ..model.model import Turmas
from .repository import TurmasRepository
from .schema import TurmasRequest, TurmasResponse

Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix = '/turmas',
    tags = ['turmas'],
    responses = {404: {"description": "Not found"}},
)

@router.post("/",
    response_model = TurmasResponse,
    status_code = status.HTTP_201_CREATED
)
def create(request: TurmasRequest, database: Session = Depends(get_database)):
    '''Cria e salva um objeto turma por meio do método POST'''
    turmas = TurmasRepository.save(database, Turmas(**request.dict()))
    return turmas


# GET ALL
@router.get("/", response_model = list[TurmasResponse])
def find_all(database: Session = Depends(get_database)):
    '''Faz uma query de todos os objetos turma na DB (sem paginação)'''
    turmas = TurmasRepository.find_all(database)
    print(turmas)
    return [TurmasResponse.from_orm(turma) for turma in turmas]


# READ BY turno
@router.get("/{turno}", response_model = TurmasResponse)
def find_by_turno(turno: str, database: Session = Depends(get_database)):
    '''Dado o Turno como parâmetro, encontra a turma com esse Turno'''
    turma = TurmasRepository.find_by_turno(database, turno)
    if not turma:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail = "turma não encontrada"
        )
    return TurmasResponse.from_orm(turma)

# READ BY id
@router.get("/{id}", response_model = TurmasResponse)
def find_by_id(id_turma: str, database: Session = Depends(get_database)):
    '''Dado o Turno como parâmetro, encontra a turma com esse Turno'''
    turma = TurmasRepository.find_by_id(database, id_turma)
    if not turma:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail = "turma não encontrada"
        )
    return TurmasResponse.from_orm(turma)

# DELETE BY id
@router.delete("/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_by_id(id: str, database: Session = Depends(get_database)):
    '''Dado o ID da turma, deleta o objeto da DB por meio do método DELETE'''
    if not TurmasRepository.exists_by_id(database, id):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, detail="turma não encontrada"
        )
    TurmasRepository.delete_by_id(database, id)
    return Response(status_code = status.HTTP_204_NO_CONTENT)

# UPDATE BY ID
@router.put("/{id}", response_model = TurmasResponse)
def update(id: str, request: TurmasRequest, database: Session = Depends(get_database)):
    '''Dado o ID da turma, atualiza os dados cadastrais na DB por meio do método PUT'''
    if not TurmasRepository.exists_by_id(database, id):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, detail = "Turma não encontrada"
        )
    turma = TurmasRepository.save(database, Turmas(id = id, **request.dict()))
    return TurmasResponse.from_orm(turma)