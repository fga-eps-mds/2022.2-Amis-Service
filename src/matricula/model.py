# '''Importando parâmetros da orm'''
# # from msilib import Table
# from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table, ForeignKeyConstraint
# # from sqlalchemy.orm import relationship
# # from src.alunas.model import Alunas
# # from src.turmas.model import Turmas

# # from src.turmas.model import Turmas
# from ..database import Base
# # from ..database import engine


# matricula = Table(
#     "matricula",
#     Base.metadata,
#     Column("idTurma", ForeignKey("turmas.idTurmas"), primary_key=True),
#     Column("idAluna", ForeignKey("alunas.idAlunas"), primary_key=True)
# )

# # class Matricula(Base):
# #     __tablename__ = "matricula"

# #     id = Column(Integer, primary_key=True, index=True)
# #     idTurma = Column(Integer, ForeignKey("turmas.id"), primary_key=True)
# #     cpfAluna = Column(String, ForeignKey("alunas.cpf"), primary_key=True)
# #     aluna = relationship("Alunas", back_populates="turma")
# #     turma: relationship("Turmas", back_populates="aluna")


# # class Turmas(Base):
# #     __tablename__ = "turmas"
# #     id = Column(Integer, primary_key=True)
# #     alunas = relationship(
# #         "Alunas", secondary=matricula
# #     )

# # class Alunas(Base):
# #     __tablename__ = "alunas"
# #     cpf = Column(String, primary_key=True)

# # Base.metadata.create_all(engine)