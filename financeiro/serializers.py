from rest_framework import serializers
from financeiro.models import (
    
    LANGUAGE_CHOICES, 
    STYLE_CHOICES,
    Fornecedor
)
import requests

class FornecedorSerializer(serializers.ModelSerializer):
    api_cnpj = serializers.SerializerMethodField()

    def get_api_cnpj(self, obj):
        dados_cnpj = requests.get(f'https://receitaws.com.br/v1/cnpj/{obj.cnpj}')
        print(dados_cnpj.json())

        return dados_cnpj.json()
    

    class Meta:
        model = Fornecedor
        fields = '__all__'
    