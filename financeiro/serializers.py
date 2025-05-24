from rest_framework import serializers
from financeiro.models import (
    
    LANGUAGE_CHOICES, 
    STYLE_CHOICES,
    Fornecedor,
    Cidade
)
import requests

class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = ['id', 'nome', 'estado']

class FornecedorSerializer(serializers.ModelSerializer):
    cidade = CidadeSerializer(read_only=True)

    class Meta:
        model = Fornecedor
        fields = '__all__'

    def validar_cnpj(self, valor):
   
        cnpj = ''.join(filter(str.isdigit, valor))

        if len(cnpj) != 14:
            raise serializers.ValidationError("CNPJ inválido.")

        api_cnpj = requests.get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj}')
        if api_cnpj.status_code != 200:
            raise serializers.ValidationError("Erro ao consultar CNPJ")
        
        dados = api_cnpj.json()
        if dados.get("status") == "ERROR":
            raise serializers.ValidationError(dados.get("message", "Erro ao consultar CNPJ."))

        # Guardando os dados
        self._dados_cnpj = {
            "logradouro" : dados.get("logradouro"),
            "numero" : dados.get("numero"),
            "bairro" : dados.get("bairro"),
            "cep" : dados.get("cep"),
            "complemento" : dados.get("complemento"),
            "telefone" : dados.get("telefone"),
            "email" : dados.get("email"),
            "logradouro" : dados.get("logradouro"),
            "atividade_principal" : dados.get("atividade_principal")
        }
        return cnpj
    
    def create(self, validated_data):
        if hasattr(self, "_dados_cnpj"):
            validated_data.update(self._dados_cnpj)

        return super().create(validated_data)
