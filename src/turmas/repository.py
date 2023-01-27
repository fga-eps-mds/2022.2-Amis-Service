from sqlalchemy.orm import Session
from ..model.model import Turmas
# from .model import Turmas

class TurmasRepository:
    @staticmethod
    def find_all(database: Session) -> list[Turmas]:
        '''Função para fazer uma query de todas as turmas da DB'''
        return database.query(Turmas).all()

    @staticmethod
    def save(database: Session, turmas: Turmas) -> Turmas:
        '''Função para salvar um objeto turma na DB'''
        if turmas.id:
            database.merge(turmas)
        else:
            database.add(turmas)
        database.commit()
        return turmas

    @staticmethod
    def find_by_turno(database: Session, turno: str) -> Turmas:
        '''Função para fazer uma query por turno de um objeto turma na DB'''
        return database.query(Turmas).filter(Turmas.turno == turno).all()

    @staticmethod
    def find_by_id(database: Session, id: str) -> Turmas:
        '''Função para fazer uma query por turma de um objeto turma na DB'''
        return database.query(Turmas).filter(Turmas.id == id).first()

    @staticmethod
    def exists_by_turno(database: Session, turno: str) -> bool:
        '''Função que verifica se o turno dado existe na DB'''
        return database.query(Turmas).filter(Turmas.turno == turno).first() is not None

    @staticmethod
    def exists_by_id(database: Session, id: int) -> bool:
        '''Função que verifica se o ID dado existe na DB'''
        return database.query(Turmas).filter(Turmas.id == id).first() is not None

    @staticmethod
    def delete_by_id(database: Session, id: str) -> None:
        '''Função para excluir um objeto turma da DB dado o ID'''
        turmas = database.query(Turmas).filter(Turmas.id == id).first()
        if turmas is not None:
            database.delete(turmas)
            database.commit()
