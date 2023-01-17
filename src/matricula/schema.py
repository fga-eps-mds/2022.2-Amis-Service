from typing import List, Union
from pydantic import BaseModel

class MatriculaBase(BaseModel):
    '''Classe para definir os modelos recebidos na API'''
    idTurma: int
    idAluna: int


class MatriculaRequest(MatriculaBase):
    '''...'''

class MatriculaResponse(MatriculaBase):
    '''...'''
    idTurma: int
    idAluna: int
    
    class Config:
        orm_mode = True
