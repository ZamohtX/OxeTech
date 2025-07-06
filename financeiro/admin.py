from django.contrib import admin
from auditlog.models import LogEntry
from django.contrib import admin
from financeiro.models.fornecedor import (
    Fornecedor,
    Cidade
)
from financeiro.models.lancamento import (
    Lancamento,
    FormaPagamento,
    Categoria
    )


# Register your models here.

class FornecedorAdmin(admin.ModelAdmin):
    model = Fornecedor

class CidadeAdmin(admin.ModelAdmin):
    model = Cidade

class LancamentoAdmin(admin.ModelAdmin):
    model = Lancamento

class FormaPagamentoAdmin(admin.ModelAdmin):
    model = FormaPagamento

class CategoriaAdmin(admin.ModelAdmin):
    model = Categoria


admin.site.register(Lancamento, LancamentoAdmin)
admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(Cidade, CidadeAdmin)
admin.site.register(FormaPagamento, FormaPagamentoAdmin)
admin.site.register(Categoria, CategoriaAdmin)




