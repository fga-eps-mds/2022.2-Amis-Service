'''Importando parâmetros da orm'''

from sqlalchemy import Column, Integer, String, ForeignKey

from ..database import Base


# matricula = Table(
#     "matricula",
#     Base.metadata,
#     Column("idTurma", ForeignKey("turmas.id"), primary_key=True),
#     Column("idAluna", ForeignKey("alunas.id"), primary_key=True)

# )

class Matricula(Base):
    __tablename__ = "matricula"

    idTurma: int = Column("idTurma", ForeignKey("turmas.id"), primary_key=True)
    idAluna: int = Column("idAluna", ForeignKey("alunas.id"), primary_key=True)

class Turmas(Base):
    '''Classe para estabelecer o modelo da tabela na DB'''
    __tablename__ = "turmas"

    id: int = Column(Integer, primary_key = True, index = True)
    descricao: str = Column(String(100), nullable = True)

class Alunas(Base):
    '''Classe para estabelecer o modelo da tabela na DB'''
    __tablename__ = "alunas"

    # UTILIZAR PARA TESTES LOCAIS
    id: int = Column(Integer, primary_key = True, index = True)
    cpf: str = Column(String(11), nullable = True)

    # UTILIZAR PARA SUBIR PARA PRODUÇÃO
    # nome: str = Column(String(100), nullable = False)
    # nomeSocial: str = Column(String(100), nullable = True)
    # rg: str = Column(String(7), nullable = False)
    # dNascimento: str = Column(String(100), nullable = False)
    # nomePai: str = Column(String(100), nullable = True)
    # nomeMae: str = Column(String(100), nullable = True)
    # deficiencia: Boolean = Column(Boolean, nullable = False)
    # idEndereco: int = Column(Integer, nullable = False)
