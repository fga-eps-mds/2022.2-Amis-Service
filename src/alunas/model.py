'''Importando parâmetros da orm'''
from sqlalchemy import Column, Integer, String, Boolean
from ..database import Base

class Alunas(Base):
    '''Classe para estabelecer o modelo da tabela na DB'''
    __tablename__ = "alunas"

    id: int = Column(Integer, primary_key = True, index = True)
    nome: str = Column(String(100), nullable = False)
    nomeSocial: str = Column(String(100), nullable = True)
    cpf: str = Column(String(11), nullable = False)
    rg: str = Column(String(7), nullable = False)
    dNascimento: str = Column(String(100), nullable = False)
    nomePai: str = Column(String(100), nullable = True)
    nomeMae: str = Column(String(100), nullable = True)
    deficiencia: Boolean = Column(Boolean, nullable = False)
    idEndereco: int = Column(Integer, nullable = False)
    #observacao: str = Column(String(200), nullable = True)
