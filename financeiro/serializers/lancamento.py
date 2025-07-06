from datetime import timedelta
from rest_framework import serializers
from financeiro.models.lancamento import Lancamento
from financeiro.repositories.lancamento import LancamentoRepository


class LancamentoSerializer(serializers.ModelSerializer):
    
    repeticoes = serializers.IntegerField(write_only=True, required=False, default=1, min_value=1)
    repository = LancamentoRepository()

    class Meta:
        model = Lancamento
        fields = [f.name for f in Lancamento._meta.fields] + ['repeticoes']

    def validate(self, attrs):
        valor = attrs.get('valor')
        valor_efetivado = attrs.get('valor_efetivado')
        vencimento = attrs.get('vencimento')
        data_efetivacao = attrs.get('data_efetivacao')

        if valor is not None and valor < 0:
            raise serializers.ValidationError("O valor não pode ser negativo.")
        if valor_efetivado is not None and valor_efetivado < 0:
            raise serializers.ValidationError("O valor efetivado não pode ser negativo.")
        if data_efetivacao and vencimento and data_efetivacao > vencimento:
            raise serializers.ValidationError("A data de efetivação não pode ser maior que o vencimento.")

        return attrs

    def create(self, validated_data):
        repeticoes = validated_data.pop('repeticoes', 1)
        vencimento_original = validated_data['vencimento']

        base_data = {
            'descricao':        validated_data['descricao'],
            'forma_pagamento':  validated_data['forma_pagamento'],
            'tipo':             validated_data['tipo'],
            'categoria':        validated_data['categoria'],
            'fornecedor':       validated_data['fornecedor'],
        }

        lancamento_principal = self.repository.create(**validated_data)

        valor = validated_data['valor']
        valor_efetivado = validated_data.get('valor_efetivado')
        if valor_efetivado is not None and valor_efetivado < valor:
            restante = valor - valor_efetivado
            dados_restante = self._build_parcela_data(
                base_data, restante, vencimento_original + timedelta(days=30)
            )
            self.repository.create(**dados_restante)

        for i in range(1, repeticoes):
            venc = vencimento_original + timedelta(days=30 * i)
            dados_rep = self._build_parcela_data(base_data, valor, venc)
            self.repository.create(**dados_rep)

        return lancamento_principal


    def _build_parcela_data(self, base_data, valor, vencimento):
     
        return {
            **base_data,
            'valor':             valor,
            'vencimento':        vencimento,
            'valor_efetivado':   None,
            'data_efetivacao':   None,
        }
