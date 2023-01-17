# '''Importando parâmetros da orm'''
# from sqlalchemy import Column, Integer, String, Boolean
# from ..database import Base
# from sqlalchemy.orm import relationship
# from ..matricula.model import matricula
# # from ..database import engine

# class Alunas(Base):
#     '''Classe para estabelecer o modelo da tabela na DB'''
#     __tablename__ = "alunas"
#     # __table_args__ = {"schema": "public"}

#     idAlunas: int = Column(Integer, primary_key = True, index = True)
#     cpf: str = Column(String(11), nullable = False)
#     nome: str = Column(String(100), nullable = False)
#     nomeSocial: str = Column(String(100), nullable = True)
#     rg: str = Column(String(7), nullable = False)
#     dNascimento: str = Column(String(100), nullable = False)
#     nomePai: str = Column(String(100), nullable = True)
#     nomeMae: str = Column(String(100), nullable = True)
#     deficiencia: Boolean = Column(Boolean, nullable = False)
#     idEndereco: int = Column(Integer, nullable = False)
#     #observacao: str = Column(String(200), nullable = True)

#     turma = relationship("Turmas", secondary=matricula, back_populates="aluna")

#     # def __repr__(self):
#     #     return f"<Alunas {self.name}>"

# # Base.metadata.create_all(engine)