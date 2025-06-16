import openpyxl
from django.core.management.base import BaseCommand, CommandError
from financeiro.models.fornecedor import Fornecedor, Cidade

class Command(BaseCommand):
    help = 'Importa fornecedores a partir de uma planilha Excel'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='O caminho do arquivo a ser importado')

    def handle(self, *args, **options):
        file_path = options['file_path']

        try:
            # carrega o arquivo
            workbook = openpyxl.load_workbook(file_path, data_only=True)
            # seleciona a primeira planilha
            sheet = workbook.active

            headers = [cell.value for cell in sheet[1]]

            header_map = {header : i for i, header in enumerate(headers)}

            for row_index, row_values in enumerate(sheet.iter_rows(min_row=2, values_only=True), start=2):
                nome_fornecedor = row_values[header_map['Nome do Fornecedor']]
                cnpj_raw = row_values[header_map['CNPJ']]
                cidade_raw = row_values[header_map['Cidade']]
                logradouro_raw = row_values[header_map['Logradouro']]

                if not nome_fornecedor or str(nome_fornecedor).strip() == '':
                    continue # Pula para a próxima linha

                cnpj_limpo = None
                if cnpj_raw is not None:
                    cnpj_limpo = str(cnpj_raw).strip().replace('.','').replace('/','').replace('-','')


                cidade_obj = None
                if cidade_raw is not None:
                    try:
                        cidade_obj = Cidade.objects.get(nome__iexact=str(cidade_raw).strip())
                    except Cidade.DoesNotExist:
                        self.stdout.write(self.style.WARNING(f"AVISO (linha {row_index}): Cidade '{cidade_raw}' não encontrada. Fornecedor '{nome_fornecedor}' será salvo sem cidade."))
                
                fornecedor, created = Fornecedor.objects.update_or_create(
                    cnpj=cnpj_limpo,
                    defaults={
                        'nome': nome_fornecedor,
                        'cidade': cidade_obj,
                        'logradouro': str(logradouro_raw) if logradouro_raw is not None else None,
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Fornecedor '{fornecedor.nome}' criado com sucesso."))
                else:
                    self.stdout.write(self.style.NOTICE(f"Fornecedor '{fornecedor.nome}' atualizado com sucesso."))

            self.stdout.write(self.style.SUCCESS('\nImportação concluída com sucesso!'))

        except FileNotFoundError:
            raise CommandError(f'Arquivo não encontrado no caminho: "{file_path}"')
        except KeyError as e:
            raise CommandError(f'Erro de Mapeamento: A coluna {e} não foi encontrada na planilha. Verifique os nomes no cabeçalho.')
        except Exception as e:
            raise CommandError(f'Ocorreu um erro durante a importação: {e}')












