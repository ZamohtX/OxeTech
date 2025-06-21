from financeiro.models.fornecedor import Fornecedor
from financeiro.repositories.base import BaseRepository


class FornecedorRepository(BaseRepository):
    def __init__(self):
        super().__init__(Fornecedor)
