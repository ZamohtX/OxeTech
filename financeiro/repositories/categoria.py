from financeiro.models.lancamento import Categoria
from financeiro.repositories.base import BaseRepository

class CategoriaRepository(BaseRepository):
    def __init__(self):
        super().__init__(Categoria)