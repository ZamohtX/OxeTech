from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from financeiro.serializers.forma_pagamento import FormaPagamentoSerializer
from financeiro.repositories.forma_pagamento import FormaPagamentoRepository


class FormaPagamentoAPIView(APIView):
    repository = FormaPagamentoRepository()

    def get(self, request, pk=None):
        if pk:
            forma_pagamento = self.repository.get_by_id(pk)
            if not forma_pagamento:
                raise Http404("Forma de pagamento não encontrada.")
            serializer = FormaPagamentoSerializer(forma_pagamento)
            return Response(serializer.data)
        
        formas_pagamento = self.repository.get_all()
        serializer = FormaPagamentoSerializer(formas_pagamento, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FormaPagamentoSerializer(data=request.data)
        if serializer.is_valid():
            forma_criada = self.repository.create(**serializer.validated_data)
            response_serializer = FormaPagamentoSerializer(forma_criada)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if not pk:
            return Response({"detail": "ID da Forma de Pagamento não informado."}, status=status.HTTP_400_BAD_REQUEST)
        
        instance = self.repository.get_by_id(pk)
        if not instance:
            raise Http404("Forma de pagamento não encontrada.")

        serializer = FormaPagamentoSerializer(instance, data=request.data)
        if serializer.is_valid():
            forma_atualizada = self.repository.update(pk, **serializer.validated_data)
            return Response(FormaPagamentoSerializer(forma_atualizada).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if not pk:
            return Response({"detail": "ID da Forma de Pagamento não informado."}, status=status.HTTP_400_BAD_REQUEST)
        
        sucesso = self.repository.delete(pk)
        if not sucesso:
            raise Http404("Forma de pagamento não encontrada.")
        return Response(status=status.HTTP_204_NO_CONTENT)
