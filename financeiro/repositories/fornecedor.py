from financeiro.models.fornecedor import Fornecedor
from financeiro.repositories.base import BaseRepository


class FornecedorRepository(BaseRepository):
    def __init__(self):
        super().__init__(Fornecedor)


    def validate(self, attrs):
        valor = attrs['valor']
        valor_efetivado = attrs['valor_efetivado']

        if valor_efetivado and valor_efetivado < valor:
            print('faça uma copia')


        return attrs
    