from typing import List, Union
from pydantic import BaseModel

class MatriculaBase(BaseModel):
    '''Classe para definir os modelos recebidos na API'''
    idTurma: int
    idAluna: str


class MatriculaRequest(MatriculaBase):
    '''...'''

class MatriculaResponse(MatriculaBase):
    '''...'''
    idTurma: int
    idAluna: str
    
    class Config:
        orm_mode = True
