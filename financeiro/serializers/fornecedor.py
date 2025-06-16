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

    cidade = CidadeSerializer(read_only=True)
    cidade_id = serializers.PrimaryKeyRelatedField(
        queryset=Cidade.objects.all(), source='cidade', write_only=True, allow_null=True
    )

    class Meta:
        model = Fornecedor
        
        # Lista explícita de campos a serem exibidos.
        fields = [
            'id', 
            'nome', 
            'cnpj',
            'logradouro',
            'cidade',
            'cidade_id',
            'dados_api_cnpj',            
            'criado_em', 
            'atualizado_em'
        ]
        
        read_only_fields = [
            'dados_api_cnpj',
            'criado_em', 
            'atualizado_em'
        ]