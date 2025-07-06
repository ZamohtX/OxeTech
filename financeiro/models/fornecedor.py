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

    
