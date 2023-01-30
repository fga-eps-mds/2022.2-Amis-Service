from ..database import engine, Base, get_db as get_database
from fastapi import APIRouter, status
from ..model.model import Ingrediente, ModoPreparo, Receita
from .repository import (
    IngredienteRepository, 
    ModoPreparoRepository, 
    ReceitasRepository
)
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
        response = ReceitasResponse(
            **response.__dict__, 
            ingredientes=[], 
            modo_preparo=[]
        )

        for ingrediente in request.ingredientes:
            ingrediente = Ingrediente(
                descricao=ingrediente, 
                receita_id=response.id
            )
            ingrediente = IngredienteRepository.save(database, ingrediente)
            response.ingredientes.append(ingrediente.descricao)
        
        for modo_preparo in request.modo_preparo:
            modo_preparo = ModoPreparo(
                descricao=modo_preparo, 
                receita_id=response.id
            )
            modo_preparo = ModoPreparoRepository.save(database, modo_preparo)
            response.modo_preparo.append(modo_preparo.descricao)

    return response

@router.get("/",
    response_model=list[ReceitasResponse],
    status_code=200
)
def get_all():
    with get_database() as database:
        response = ReceitasRepository.find_all(database)
    return response

@router.get("/{receita_id}",
    response_model=ReceitasResponse,
    status_code=200
)
def get_by_id(receita_id: int):
    with get_database() as database:
        response = ReceitasRepository.find_by_id(database, receita_id)
    return response