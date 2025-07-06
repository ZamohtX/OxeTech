from django.db import models
from financeiro.models.fornecedor import (
    Base,
    Fornecedor
)



class FormaPagamento(Base):
    nome = models.CharField(max_length=50, blank=False, null=False)
    
    
class Categoria(Base):
    nome = models.CharField(max_length=50, blank=False, null=False)
    
    
class Lancamento(Base):
    ENTRADA = 'E'
    SAIDA = 'S'

    TIPO_LANCAMENTO = (
        (ENTRADA, 'Entrada'),
        (SAIDA, 'Saída')
    )
    
    descricao = models.TextField(blank=False, null=False)
    forma_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.PROTECT)
    tipo = models.CharField(max_length=1, blank=False, null=False, choices=TIPO_LANCAMENTO)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    valor = models.DecimalField(max_digits=9, decimal_places=2, blank=False, null=False)
    valor_efetivado = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    vencimento = models.DateField(blank=False, null=False)
    data_efetivacao = models.DateField(blank=True, null=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT)
