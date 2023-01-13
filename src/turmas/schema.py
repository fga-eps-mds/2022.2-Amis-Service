#from typing import Union
from pydantic import BaseModel

class TurmasBase(BaseModel):
    '''Classe para definir os modelos recebidos na API'''
    descricao: str 
    turno: str 
    capacidade: int 
    horarioInicio: str  
    horarioFim: str  
    dataInicio: str  
    dataFim: str
    
class TurmasRequest(TurmasBase):
    '''...'''

class TurmasResponse(TurmasBase):
    '''...'''
    turno: str
    id: int
    class Config:
        orm_mode = True
