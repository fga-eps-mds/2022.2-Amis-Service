'''Importando parâmetros da orm'''
from sqlalchemy import Column, Integer, String, Enum
from ..database import Base

class Turmas(Base):
    '''Classe para estabelecer o modelo da tabela na DB'''
    __tablename__ = "turmas"

    id: int = Column(Integer, primary_key = True, index = True)
    descricao: str = Column(String(100), nullable = True)
    turno: str = Column(Enum('1','2','3'), nullable = False) #Verificar se troca para matutino,vespertino e noturno
    capacidade: int = Column(Integer, nullable = False)
    horarioInicio: str = Column(String(100), nullable = True) # alterar para time
    horarioFim: str = Column(String(100), nullable = True) # alterar para time
    dataInicio: str = Column(String(100), nullable = True) # alterar para time
    dataFim: str = Column(String(100), nullable = True) # alterar para time