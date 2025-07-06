from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from financeiro.serializers.lancamento import LancamentoSerializer
from financeiro.repositories.lancamento import LancamentoRepository


class LancamentoAPIView(APIView):
    repository = LancamentoRepository()

    def get(self, request, pk=None):
        if pk:
            lancamento = self.repository.get_by_id(pk)
            if not lancamento:
                raise Http404("Lançamento não encontrado.")
            serializer = LancamentoSerializer(lancamento)
            return Response(serializer.data)
        
        lancamentos = self.repository.get_all()
        serializer = LancamentoSerializer(lancamentos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LancamentoSerializer(data=request.data)
        if serializer.is_valid():
            lancamento_criado = serializer.save()  
            response_serializer = LancamentoSerializer(lancamento_criado)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if not pk:
            return Response({"detail": "ID do lançamento não informado."}, status=status.HTTP_400_BAD_REQUEST)
        
        instance = self.repository.get_by_id(pk)
        if not instance:
            raise Http404("Lançamento não encontrado.")

        serializer = LancamentoSerializer(instance, data=request.data)
        if serializer.is_valid():
            lancamento_atualizado = self.repository.update(pk, **serializer.validated_data)
            return Response(LancamentoSerializer(lancamento_atualizado).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if pk:
            sucesso = self.repository.delete(pk)
            if not sucesso:
                raise Http404("Lançamento não encontrado.")
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        sucesso = self.repository.delete_all()
        if not sucesso:
            return Response({"detail": "Nenhum lançamento para deletar."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)