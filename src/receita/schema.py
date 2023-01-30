from typing import Union
from pydantic import BaseModel
from datetime import datetime

class ReceitasBase(BaseModel):
    '''Classe para definir os modelos recebidos na API'''
    nome: str


class ReceitasRequest(ReceitasBase):
    ingredientes: list[str]
    modo_preparo: list[str]
    '''...'''

class ReceitasResponse(ReceitasBase):
    '''...'''
    id: int
    created_at: datetime
    ingredientes: list
    # modo_preparo: list[str]
    class Config:
        orm_mode = True
