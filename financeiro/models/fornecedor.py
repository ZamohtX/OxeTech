from django.db import models

        
class Base(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Estado(models.Model):
    nome = models.CharField(blank=False, null=False, max_length=50)
    uf = models.CharField(blank=False, null=False, max_length=2)
    
    def __str__(self):
        return self.nome    
    
    
class Cidade(models.Model):
    nome = models.CharField(blank=False, null=False, max_length=100)
    estado = models.ForeignKey(Estado,  on_delete=models.PROTECT, blank=False, null=True)
    
    
class Fornecedor(Base):
    nome = models.CharField(blank=False, null=False, max_length=200)
    cnpj = models.CharField(blank=True, null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT, blank=True, null=True)
    logradouro = models.CharField(blank=True, null=True)
    dados_api_cnpj = models.JSONField(null=True, blank=True)

    
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
