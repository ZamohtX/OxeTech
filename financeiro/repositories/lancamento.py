from financeiro.models.lancamento import Lancamento
from financeiro.repositories.base import BaseRepository


class LancamentoRepository(BaseRepository):
    def __init__(self):
        super().__init__(Lancamento)