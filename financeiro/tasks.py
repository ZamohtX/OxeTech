from celery import shared_task
import requests
from financeiro.models.fornecedor import Fornecedor

@shared_task
def consultar_e_atualizar_cnpj(pk):
    try:
        fornecedor = Fornecedor.objects.get(id=pk)
    except Fornecedor.DoesNotExist:
        return f"Fornecedor com ID {pk} não encontrado."
    
    if not fornecedor.cnpj:
        return f"Fornecedor {pk} não possui CNPJ"
    
    cnpj_limpo = str(fornecedor.cnpj).strip().replace('.','').replace('/','').replace('-', '')

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        fornecedor.dados_api_cnpj = response.json()
        fornecedor.save(update_fields=['dados_api_cnpj'])
        return f"CNPJ de {fornecedor.nome} atualizado com sucesso"
    except requests.exceptions.RequestException as e:
        return f"falha ao consultar CNPJ para o fonecedor {pk} : {e}"