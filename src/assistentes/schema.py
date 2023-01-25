from typing import Union
from pydantic import BaseModel

class AssistentesBase(BaseModel):
    '''Classe para definir os modelos recebidos na API'''
    nome: str
    cpf: Union[str, None] = None
    login: str
    ##senha: str
    observacao: str
    administrador: bool

class AssistentesRequest(AssistentesBase):
    '''...'''

class AssistentesResponse(AssistentesBase):
    '''...'''
    cpf: str
    id: int
    class Config:
        orm_mode = True
