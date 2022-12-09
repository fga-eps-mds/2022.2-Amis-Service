from sqlalchemy.orm import Session
from alunas.model import Alunas

class AlunasRepository:
    @staticmethod
    def find_all(database: Session) -> list[Alunas]:
        '''Função para fazer uma query de todas as alunas da DB'''
        return database.query(Alunas).all()

    @staticmethod
    def save(database: Session, alunas: Alunas) -> Alunas:
        '''Função para salvar um objeto aluna na DB'''
        if alunas.id:
            database.merge(alunas)
        else:
            database.add(alunas)
        database.commit()
        return alunas

    @staticmethod
    def find_by_cpf(database: Session, cpf: str) -> Alunas:
        '''Função para fazer uma query por CPF de um objeto aluna na DB'''
        return database.query(Alunas).filter(Alunas.cpf == cpf).first()

    @staticmethod
    def exists_by_cpf(database: Session, cpf: str) -> bool:
        '''Função que verifica se o CPF dado existe na DB'''
        return database.query(Alunas).filter(Alunas.cpf == cpf).first() is not None

    @staticmethod
    def exists_by_id(database: Session, id: int) -> bool:
        '''Função que verifica se o ID dado existe na DB'''
        return database.query(Alunas).filter(Alunas.id == id).first() is not None

    @staticmethod
    def delete_by_id(database: Session, id: str) -> None:
        '''Função para excluir um objeto aluna da DB dado o ID'''
        alunas = database.query(Alunas).filter(Alunas.id == id).first()
        if alunas is not None:
            database.delete(alunas)
            database.commit()
