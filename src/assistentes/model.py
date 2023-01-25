# '''Importando parâmetros da orm'''
# from sqlalchemy import Column, Integer, String, Boolean
# from ..database import Base

# class Assistentes(Base):
#     '''Classe para estabelecer o modelo da tabela na DB'''
#     __tablename__ = "assistentes"

#     id: int = Column(Integer, primary_key = True, index = True)
#     nome: str = Column(String(100), nullable = False)
#     login: str = Column(String(100), nullable = False)
#     ##senha: bcrypt str = Column(String(100), nullable = False)
#     cpf: str = Column(String(11), nullable = False)
#     observacao: str = Column(String(200), nullable = True)
#     administrador: bool = Column(Boolean, nullable = False)
