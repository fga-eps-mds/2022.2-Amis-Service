# '''Importando parâmetros da orm'''
# from sqlalchemy import Column, Integer, String, Enum
# from sqlalchemy.orm import relationship
# from ..matricula.model import matricula

# # from src.alunas.model import Alunas
# from ..database import Base
# # from ..database import engine
# # from ..matricula.model import matricula

# class Turmas(Base):
#     '''Classe para estabelecer o modelo da tabela na DB'''
#     __tablename__ = "turmas"
#     # __table_args__ = {"schema": "public"}

#     idTurmas: int = Column(Integer, primary_key = True, index = True)
#     descricao: str = Column(String(100), nullable = True)
#     # turno: str = Column(Enum('1','2','3'), nullable = False) #Verificar se troca para matutino,vespertino e noturno
#     # capacidade: int = Column(Integer, nullable = False)
#     # horarioInicio: str = Column(String(100), nullable = True) # alterar para time
#     # horarioFim: str = Column(String(100), nullable = True) # alterar para time
#     # dataInicio: str = Column(String(100), nullable = True) # alterar para time
#     # dataFim: str = Column(String(100), nullable = True) # alterar para time

#     aluna = relationship("Alunas", secondary=matricula, back_populates="turma")

#     # def __repr__(self):
#     #     return f"<Turmas {self.name}>"

# # Base.metadata.create_all(engine)