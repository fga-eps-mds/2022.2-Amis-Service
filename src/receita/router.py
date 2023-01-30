from sqlalchemy.orm import Session
from ..database import engine, Base, get_db as get_database
from fastapi import APIRouter, status, HTTPException, Response, Depends
from ..model.model import Ingrediente, Receita
from .repository import IngredienteRepository, ReceitasRepository
from .schema import ReceitasRequest, ReceitasResponse

Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix = '/receita',
    tags = ['receita'],
    responses = {404: {"description": "Not found"}},
)

@router.post("/",
    response_model=ReceitasResponse,
    status_code = status.HTTP_201_CREATED
)
def create(request: ReceitasRequest):
    with get_database() as database:
        response = ReceitasRepository.save(database, Receita(request.__dict__))
        response = ReceitasResponse(**response.__dict__, ingredientes=[], modo_preparo=[])

        for ingrediente in request.ingredientes:
            ingrediente = Ingrediente(descricao=ingrediente, receita_id=response.id)
            ingrediente = IngredienteRepository.save(database, ingrediente)
            response.ingredientes.append(ingrediente.descricao)
    return response

@router.get("/",
    response_model=list[ReceitasResponse],
    status_code=200
)
def get_all():
    with get_database() as database:
        response = ReceitasRepository.find_all(database)
    return response