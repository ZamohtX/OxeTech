from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from financeiro.models.lancamento import Categoria
from financeiro.repositories.categoria import CategoriaRepository
from financeiro.serializers.categoria import CategoriaSerializer


class CategoriaAPIView(APIView):
    repository = CategoriaRepository()

    def get(self, resquest, pk=None):
        if pk:
            categoria = self.repository.get_by_id(pk)
            if not categoria:
                raise Http404("Categoria não encontrada.")
            serializer = CategoriaSerializer(categoria)
            return Response(serializer.data)
        
        categorias = self.repository.get_all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            categoria_criada = serializer.save()
            response_serializer = CategoriaSerializer(categoria_criada)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        if not pk:
            return Response({"detail" : "ID da categoria é obrigatório"},
                            status=status.HTTP_400_BAD_REQUEST)
        categoria = self.repository.get_by_id(pk)
        if not categoria:
            raise Http404("Categoria não encontada.")
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            categoria_atualizada = self.repository.update(pk, **serializer.validated_data)
            return Response(CategoriaSerializer(categoria_atualizada).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        if pk:
            sucesso = self.repository.delete(pk)
            if not sucesso:
                raise Http404("Categoria não encontrada.")
            return Response(status=status.HTTP_204_NO_CONTENT)
        sucesso = self.repository.delete_all()
        if not sucesso:
            return Response({"detail" : "Nenhuma categoria para deletar"},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)