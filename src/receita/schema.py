from typing import Union
from pydantic import BaseModel
from datetime import datetime

class ReceitasBase(BaseModel):
    '''Classe para definir os modelos recebidos na API'''
    nome: str
    id: Union[None, int]


class ReceitasRequest(ReceitasBase):
    '''Classe para definir o modelo das requisicoes'''
    ingredientes: list[str]
    modo_preparo: list[str]

class ReceitasResponse(ReceitasBase):
    '''Classe para definir o modelo das respostas'''
    created_at: Union[datetime, None]
    ingredientes: list
    modo_preparo: list
    class Config:
        orm_mode = True
