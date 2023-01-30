from sqlalchemy.orm import Session
from ..model.model import Receita, Ingrediente

class ReceitasRepository:
    @staticmethod
    def save(database: Session, receita_object: Receita, receita_id: int = None) -> Receita:
        '''Função para salvar um objeto assistente na DB'''
        if receita_id:
            database.merge(receita_object)
        else:
            database.add(receita_object)
        database.flush()
        database.commit()
        return receita_object
    
    def find_all(database: Session) -> list[Receita]:
        '''Funcao para encontrar todas as receitas'''
        response = database.query(Receita).all()
        return response
        

class IngredienteRepository:
    @staticmethod
    def save(database: Session, ingrediente_object: Ingrediente, ingrediente_id: int = None) -> Ingrediente:
        '''Função para salvar um objeto assistente na DB'''
        if ingrediente_id:
            database.merge(ingrediente_object)
        else:
            database.add(ingrediente_object)
        database.commit()
        return ingrediente_object