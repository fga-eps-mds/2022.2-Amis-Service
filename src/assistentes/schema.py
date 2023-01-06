from typing import Union
from pydantic import BaseModel

class AssistentesBase(BaseModel):
    '''Classe para definir os modelos recebidos na API'''
    nome: str
    nomeSocial: str
    cpf: Union[str, None] = None
    rg: Union[str, None] = None
    dNascimento: str
    nomePai: str
    nomeMae: str
    deficiencia: bool
    idEndereco: int
    #observacao: str

class AssistentesRequest(AssistentesBase):
    '''...'''

class AssistentesResponse(AssistentesBase):
    '''...'''
    cpf: str
    id: int
    class Config:
        orm_mode = True
