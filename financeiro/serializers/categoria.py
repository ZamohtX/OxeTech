from rest_framework import serializers
from financeiro.models.lancamento import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

        



