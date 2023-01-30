'''Importando parâmetros da orm'''

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Enum, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from ..database import Base

class Matricula(Base):
    __tablename__ = "matricula"

    idTurma: int = Column("idTurma", ForeignKey("turmas.id"), primary_key=True)
    idAluna: int = Column("idAluna", ForeignKey("alunas.id"), primary_key=True)

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

class Alunas(Base):
    '''Classe para estabelecer o modelo da tabela na DB'''
    __tablename__ = "alunas"

    # UTILIZAR PARA TESTES LOCAIS
    id: int = Column(Integer, primary_key = True, index = True)
    cpf: str = Column(String(11), nullable = True)

    # UTILIZAR PARA SUBIR PARA PRODUÇÃO
    nome: str = Column(String(100), nullable = False)
    nomeSocial: str = Column(String(100), nullable = True)
    rg: str = Column(String(7), nullable = False)
    dNascimento: str = Column(String(100), nullable = False)
    nomePai: str = Column(String(100), nullable = True)
    nomeMae: str = Column(String(100), nullable = True)
    deficiencia: Boolean = Column(Boolean, nullable = False)
    idEndereco: int = Column(Integer, nullable = False)
    formada: Boolean = Column(Boolean, nullable = False)

class Assistentes(Base):
    '''Classe para estabelecer o modelo da tabela na DB'''
    __tablename__ = "assistentes"

    id: int = Column(Integer, primary_key = True, index = True)
    nome: str = Column(String(100), nullable = False)
    login: str = Column(String(100), nullable = False)
    ##senha: bcrypt str = Column(String(100), nullable = False)
    cpf: str = Column(String(11), nullable = False)
    observacao: str = Column(String(200), nullable = True)
    administrador: bool = Column(Boolean, nullable = False)

class Receita(Base):
    '''Classe para estabelecer o modelo da tabela na DB'''
    __tablename__ = "receita"

    def __init__(self, receita: dict) -> None:
        self.nome = receita['nome']
        
    id: int = Column(
        Integer, 
        primary_key = True, 
        index = True, 
        autoincrement=True
    )
    nome: str = Column(String(100), nullable = False)
    ingredientes = relationship('Ingrediente', backref='Receita', lazy='joined')
    modo_preparo = relationship('ModoPreparo', backref='Receita', lazy='joined')

    created_at = Column(DateTime, default=datetime.now())

class Ingrediente(Base):
    """Tabela para representar um ingrediente na receita"""
    __tablename__ = "ingrediente"

    id: int =  Column(
        Integer, 
        primary_key = True, 
        index = True, 
        autoincrement=True
    )
    receita_id: int = Column(
        Integer, 
        ForeignKey("receita.id"), 
        index=True, 
        nullable=False
    )
    descricao: str = Column(String(100), nullable=False) 

class ModoPreparo(Base):
    """Tabela para representar um ingrediente na receita"""
    __tablename__ = "modo_preparo"

    id: int =  Column(
        Integer, 
        primary_key = True, 
        index = True,
        autoincrement=True
    )
    receita_id: int = Column(
        Integer, 
        ForeignKey("receita.id"), 
        index=True, 
        nullable=False
    )
    descricao: str = Column(String(100), nullable=False) 

    