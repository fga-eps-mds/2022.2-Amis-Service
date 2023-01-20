from sqlalchemy.orm import Session

from src.alunas.repository import AlunasRepository
from ..model.model import Matricula
# from ..model.model import matricula
# from .model import matricula

class MatriculaRepository:
    @staticmethod
    def save(database: Session, novaMatricula: Matricula) -> Matricula:
        '''Função para salvar um objeto matricula na DB'''
        idsAluna = novaMatricula.idAluna.split(',')
        idAlunaReturn = []
        
        for id in idsAluna:
            if (AlunasRepository.exists_by_id(database, id)):
                if novaMatricula.idTurma:
                    novaMatricula.idAluna = int(id) 
                    database.merge(novaMatricula)
                    database.commit()
                    idAlunaReturn.append(id)

                else:
                    novaMatricula.idAluna = int(id)
                    database.add(novaMatricula)
                    database.commit()
                    idAlunaReturn.append(id)
            else:
                raise Exception("Aluna id" + id + " não matriculada.")


        novaMatricula.idAluna = ','.join(idAlunaReturn)
        return novaMatricula
    
    @staticmethod
    def find_all(database: Session) -> list[Matricula]:
        '''Função para fazer uma query de todas as alunas da DB'''
        return database.query(Matricula).all()

    @staticmethod
    def find_by_id(database: Session, id: str) -> Matricula:
        '''Função para fazer uma query por ID de um objeto Matricula na DB'''
        return database.query(Matricula).filter(Matricula.idTurma == id).all()

    @staticmethod
    def exists_by_id(database: Session, idTurma: int, idAluna: int) -> bool:
        '''Função que verifica se a turma e aluna existe pelo ID dado na DB'''
        turma = database.query(Matricula).filter(Matricula.idTurma == idTurma, Matricula.idAluna == idAluna).first()
        print(turma.idTurma, turma.idAluna)
        return turma is not None

    @staticmethod
    def delete_by_id(database: Session, idTurma: str, idAluna: str) -> None:
        '''Função para excluir uma aluna da turma no DB dado seu ID'''
        aluna = database.query(Matricula).filter(Matricula.idTurma == idTurma and Matricula.idAluna == idAluna).first()
        if aluna is not None:
            database.delete(aluna)
            database.commit()
            # database.flush()
