from sqlalchemy.orm import Session, exc
from ..model.model import ModoPreparo, Receita, Ingrediente

class ReceitasRepository:
    @staticmethod
    def save(
        database: Session, 
        receita_object: Receita, 
        receita_id: int = None
    ) -> Receita:
        '''Função para salvar um objeto assistente na DB'''
        if receita_id:
            receita_object.id = receita_id
            database.merge(receita_object)
        else:
            database.add(receita_object)
        database.flush()
        database.commit()
        return receita_object
    
    @staticmethod
    def find_all(database: Session) -> list[Receita]:
        '''Funcao para encontrar todas as receitas'''
        response = database.query(Receita).all()
        return response
    
    @staticmethod
    def find_by_id(database: Session, receita_id: int) -> list[Receita]:
        '''Funcao para encontrar uma receita pelo id'''
        response = database.query(Receita).filter(
            Receita.id == receita_id
            ).first()
        return response
    
    @staticmethod
    def delete_by_id(database: Session, receita_id: int) -> None:
        '''Funcao para deletar as Receitas pelo id'''
        receita = ReceitasRepository.find_by_id(database, receita_id)

        if receita is not None:
            database.delete(receita)
            database.commit()
        else:
            raise exc.NoResultFound
        

class IngredienteRepository:
    @staticmethod
    def save(
        database: Session, 
        ingrediente_object: Ingrediente, 
        ingrediente_id: int = None
    ) -> Ingrediente:
        '''Função para salvar um objeto assistente na DB'''
        if ingrediente_id:
            database.merge(ingrediente_object)
        else:
            database.add(ingrediente_object)
        database.commit()
        return ingrediente_object

class ModoPreparoRepository:
    @staticmethod
    def save(
        database: Session, 
        modo_preparo_object: ModoPreparo, 
        modo_preparo_id: int = None
    ) -> ModoPreparo:
        '''Funcao que salva ou atualiza um modo de preparo'''

        if modo_preparo_id:
            database.merge(modo_preparo_object)
        else:
            database.add(modo_preparo_object)
        database.commit()
        return modo_preparo_object