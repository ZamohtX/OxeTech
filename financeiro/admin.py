from django.contrib import admin
from auditlog.models import LogEntry
from django.contrib import admin
from financeiro.models.fornecedor import Fornecedor

# Register your models here.

class FornecedorAdmin(admin.ModelAdmin):
    model = Fornecedor



admin.site.register(Fornecedor, FornecedorAdmin)