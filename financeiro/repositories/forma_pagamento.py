from financeiro.models.lancamento import FormaPagamento
from financeiro.repositories.base import BaseRepository


class FormaPagamentoRepository(BaseRepository):
    def __init__(self):
        super().__init__(FormaPagamento)