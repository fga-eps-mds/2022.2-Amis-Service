#from typing import Union
from pydantic import BaseModel

class TurmasBase(BaseModel):
    '''Classe para definir os modelos recebidos na API'''
    # UTILIZAR PARA TESTES LOCAIS
    descricao: str 

    # UTILIZAR PARA SUBIR PARA PRODUÇÃO
    # descricao: str 
    # turno: str 
    # capacidade: int 
    # horarioInicio: str  
    # horarioFim: str  
    # dataInicio: str  
    # dataFim: str
    
class TurmasRequest(TurmasBase):
    '''...'''

class TurmasResponse(TurmasBase):
    '''...'''
    id: int
    class Config:
        orm_mode = True
