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
        try:
            dados_cnpj = requests.get(f'https://receitaws.com.br/v1/cnpj/{obj.cnpj}')

            return dados_cnpj.json()
        except Exception as error:
            print(error)
            pass
    
    class Meta:
        model = Fornecedor
        fields = '__all__'