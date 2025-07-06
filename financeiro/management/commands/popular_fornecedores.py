
import xlrd 
import os
from django.core.management.base import BaseCommand, CommandError
from financeiro.models.fornecedor import Fornecedor, Cidade
from financeiro.repositories.fornecedor import FornecedorRepository
from financeiro.tasks import enviar_email

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        current_dir = os.path.dirname(__file__)
        path  = os.path.join(current_dir, "myfile.xls")
        book = xlrd.open_workbook(path)
        
        sh = book.sheet_by_index(0)
        
        for rx in range(sh.nrows):
            if rx > 0:
                nome = sh.row(rx)[0].value
                cnpj = sh.row(rx)[1].value
                cidade = Cidade.objects.get(id=1)
                objeto, _ = Fornecedor.objects.get_or_create(
                        nome = nome,
                        cnpj = cnpj,
                        cidade = cidade,
                        defaults={
                            "logradouro": "Desconhecido"
                        }
                    )
                
        email_enviado = enviar_email.delay(
            destinatario='juniorgamer009@gmail.com',
            assunto='Relatorio de Cadastro',
            mensagem='Fornecedores Cadastrados'
        )



