from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from financeiro.serializers.fornecedor import FornecedorSerializer
from financeiro.repositories.fornecedor import FornecedorRepository
from financeiro.tasks import consultar_e_atualizar_cnpj


class FornecedorAPIView(APIView):
    
    repository = FornecedorRepository()

    def get(self, request, pk=None):
        if pk:
            fornecedor = self.repository.get_by_id(pk)
            if not fornecedor:
                raise Http404("Fornecedor não encontrado.")
            serializer = FornecedorSerializer(fornecedor)
            return Response(serializer.data)
        else:
            fornecedores  = self.repository.get_all()
            serializer = FornecedorSerializer(fornecedores, many= True)
            return Response(serializer.data)
        
    def post(self, request):
        serializer = FornecedorSerializer(data=request.data)
        if serializer.is_valid():
            novo_fornecedor = self.repository.create(serializer.validated_data)
            if novo_fornecedor.cnpj:
                consultar_e_atualizar_cnpj.delay(novo_fornecedor.pk)
            response_serializer = FornecedorSerializer(novo_fornecedor)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, pk=None):
        instance = self.repository.get_by_id(pk)
        if not instance:
            raise Http404("Fornecedor não encontrado.")
        
        serializer = FornecedorSerializer(instance, data=request.data)
        if serializer.is_valid():
            fornecedor_atualizado = self.repository.update(pk, serializer.validated_data)
            return Response(FornecedorSerializer(fornecedor_atualizado).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk=None):
        sucesso = self.repository.delete(pk)
        if not sucesso:
            raise Http404("Fornecedor não encontrado.")
        return Response(status=status.HTTP_204_NO_CONTENT)






