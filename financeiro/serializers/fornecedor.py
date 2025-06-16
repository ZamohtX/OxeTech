from rest_framework import serializers
from financeiro.models.fornecedor import (
    Cidade,
    Fornecedor
)
import requests
    
class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = ['nome', 'estado']
    
class FornecedorSerializer(serializers.ModelSerializer):
    api_cnpj = serializers.SerializerMethodField()
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['cidade'] = CidadeSerializer(instance.cidade).data
        return rep
        
    def get_api_cnpj(self, obj):
        if not obj or not obj.cnpj:
            return None
        try:
            cnpj_limpo = str(obj.cnpj).strip().replace('.', '').replace('/', '').replace('-', '')
        except AttributeError:
            return {"error": "O valor do CNPJ não é válido."}

        try:
            url = f'https://receitaws.com.br/v1/cnpj/{cnpj_limpo}'
            response = requests.get(url, timeout=10) # Timeout de 10 segundos
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            return {"error": "A consulta ao CNPJ demorou muito para responder (timeout)."}        
        except requests.exceptions.HTTPError as http_err:
            status_code = http_err.response.status_code
            if status_code == 429:
                return {"error": "Muitas requisições. O limite da API de CNPJ foi excedido."}
            if status_code == 404:
                return {"error": "CNPJ não encontrado na base de dados da ReceitaWS."}
            return {"error": f"Erro na API de CNPJ. Status: {status_code}."} 
        except requests.exceptions.RequestException as req_err:
            return {"error": f"Erro de rede ao consultar o CNPJ: {req_err}"}

    class Meta:
        model = Fornecedor
        fields = '__all__'