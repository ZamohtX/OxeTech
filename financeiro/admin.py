from django.contrib import admin
from auditlog.models import LogEntry
from django.contrib import admin
from financeiro.models.fornecedor import Fornecedor
from financeiro.models.fornecedor import Cidade

# Register your models here.

class FornecedorAdmin(admin.ModelAdmin):
    model = Fornecedor

class CidadeAdmin(admin.ModelAdmin):
    model = Cidade


admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(Cidade, CidadeAdmin)





