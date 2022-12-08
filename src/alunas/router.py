from .model import Alunas
from .repository import AlunasRepository
from .schema import AlunasRequest, AlunasResponse
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from fastapi import APIRouter, status, HTTPException, Response, Depends

Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix='/alunas',
    tags=['alunas'],
    responses={404: {"description": "Not found"}},
)

@router.post("/",
    response_model=AlunasResponse,
    status_code=status.HTTP_201_CREATED
)
def create(request: AlunasRequest, db: Session = Depends(get_db)):
    alunas = AlunasRepository.save(db, Alunas(**request.dict()))
    return alunas


# GET ALL
@router.get("/", response_model=list[AlunasResponse])
def find_all(db: Session = Depends(get_db)):
    alunas = AlunasRepository.find_all(db)
    print(alunas)
    return [AlunasResponse.from_orm(aluna) for aluna in alunas]


# READ BY cpf
@router.get("/{cpf}", response_model=AlunasResponse)
def find_by_cpf(cpf: str, db: Session = Depends(get_db)):
    aluna = AlunasRepository.find_by_cpf(db, cpf)
    if not aluna:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="aluna não encontrada"
        )
    return AlunasResponse.from_orm(aluna)

# DELETE BY id
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: str, db: Session = Depends(get_db)):
    if not AlunasRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="aluna não encontrada"
        )
    AlunasRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# UPDATE BY ID
@router.put("/{id}", response_model=AlunasResponse)
def update(id: str, request: AlunasRequest, db: Session = Depends(get_db)):
    if not AlunasRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Aluna não encontrada"
        )
    aluna = AlunasRepository.save(db, Alunas(id=id, **request.dict()))
    return AlunasResponse.from_orm(aluna)