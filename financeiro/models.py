from django.db import models
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Base(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    historico = AuditlogHistoryField()  
    
    class Meta:
        abstract = True



class Estado(models.Model):
    nome = models.CharField(blank=False, null=False, max_length=50)
    uf = models.CharField(blank=False, null=False, max_length=2)

    historico = AuditlogHistoryField()  

    def __str__(self):
        return self.nome

class Cidade(models.Model):
    nome = models.CharField(blank=False, null=False, max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, blank=False, null=True)

    historico = AuditlogHistoryField() 

    def __str__(self):
        return self.nome


class Fornecedor(Base):
    nome = models.CharField(blank=False, null=False, max_length=200)
    cnpj = models.CharField(blank=True, null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT, blank=False, null=False)

    historico = AuditlogHistoryField()  # Isso cria os logs





auditlog.register(Base)
auditlog.register(Cidade)
auditlog.register(Estado)
auditlog.register(Fornecedor)

