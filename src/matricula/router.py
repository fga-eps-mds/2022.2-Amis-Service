from typing import List
from sqlalchemy.orm import Session
from ..database import engine, Base, get_db as get_database
from fastapi import APIRouter, status, HTTPException, Response, Depends
# from ..model.model import matricula
from ..model.model import Matricula
from .repository import MatriculaRepository
from .schema import MatriculaRequest, MatriculaResponse
from ..alunas.repository import AlunasRepository
from ..turmas.repository import TurmasRepository

Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix = '/matricula',
    tags = ['matricula'],
    responses = {404: {"description": "Not found"}},
)

# GET ALL
@router.get("/", response_model = list[MatriculaResponse])
def find_all(database: Session = Depends(get_database)):
    '''Faz uma query de todos os objetos matricula na DB (sem paginação)'''
    matricula = MatriculaRepository.find_all(database)
    return [MatriculaResponse.from_orm(matricula) for matricula in matricula]

# CREATE
@router.post("/",
    response_model = MatriculaResponse,
    status_code = status.HTTP_201_CREATED
)
def create(request: MatriculaRequest, database: Session = Depends(get_database)):
    '''Cria e salva um objeto matricula por meio do método POST'''
    try:
        novaMatricula = MatriculaRepository.save(database, Matricula(**request.dict()))
        return novaMatricula
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail = str(error)
        )

# FIND BY ID
@router.get("/{id}", response_model = {})
def find_by_id(id: str, database: Session = Depends(get_database)):
    '''Dado o ID como parâmetro, encontra a matricula com esse ID'''
    matricula = MatriculaRepository.find_by_id(database, id)

    if not matricula:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail = "Matricula não encontrada"
        )

    returnMatricula = []

    for m in matricula:
        aluna = AlunasRepository.find_by_id(database, m.idAluna)
        returnMatricula.append(
            aluna
        )

    return returnMatricula

# DELETE BY id
@router.delete("/{idTurma}/{idAluna}", status_code = status.HTTP_204_NO_CONTENT)
def delete_by_id(idTurma: str, idAluna: str, database: Session = Depends(get_database)):
    '''Dado o ID da turma e aluna, deleta o objeto da DB por meio do método DELETE'''
    if not MatriculaRepository.exists_by_id(database, idTurma, idAluna):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, detail="Turma/Aluna não encontrada"
        )
    
    MatriculaRepository.delete_by_id(database, idTurma, idAluna)
    return Response(status_code = status.HTTP_204_NO_CONTENT)

# CONSULTAR VAGAS TOTAIS E PREENCHIDAS NA TURMA BY ID
@router.get("/turma/{id}", response_model = {})
def find_qtd_vagas_by_id(id: str, database: Session = Depends(get_database)):
    '''Dado o ID como parâmetro, retorna a qtd de matricula nessa turma'''

    turma = TurmasRepository.find_by_id(database, id)
    if not turma:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail = "Turma não encontrada"
        )
    print(turma)
    vagasTotais = turma.capacidade
    matricula = len(MatriculaRepository.find_by_id(database, id))
    vagasDisponiveis = vagasTotais - matricula

    vagas = {
        "vagasTotais": vagasTotais,
        "vagasDisponiveis": vagasDisponiveis
    }

    return vagas