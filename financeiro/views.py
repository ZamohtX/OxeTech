from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from financeiro.models import (
    Fornecedor,
    Cidade,
    Estado  
)
from financeiro.serializers import (
    FornecedorSerializer,
    CidadeSerializer,
    EstadoSerializer
)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def fornecedor_list(request):
    if request.method == 'GET':
        fornecedores = Fornecedor.objects.all()
        serializer = FornecedorSerializer(fornecedores, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FornecedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def fornecedor_detail(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)

    if request.method == 'GET':
        serializer = FornecedorSerializer(fornecedor)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = FornecedorSerializer(fornecedor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        fornecedor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def cidade_list(request):
    if request.method == 'GET':
        cidades = Cidade.objects.all()
        serializer = CidadeSerializer(cidades, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CidadeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def cidade_detail(request, pk):
    try:
        cidade = get_object_or_404(Cidade, pk=pk)
    except Cidade.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CidadeSerializer(cidade)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        cidade.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def estado_list(request):
    if request.method == 'GET':
        estados = Estado.objects.all()
        serializer = EstadoSerializer(estados, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = EstadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','DELETE'])
def estado_detail(request, pk):
    try:
        estado = Estado.objects.get(pk=pk)
    except Estado.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = EstadoSerializer(estado)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        estado.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    