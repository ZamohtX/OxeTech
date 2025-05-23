from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from financeiro.models import Fornecedor  
from financeiro.serializers import FornecedorSerializer 

@csrf_exempt
def fornecedor_list(request):

    if request.method == 'GET':
        fornecedores = Fornecedor.objects.all()
        serializer = FornecedorSerializer(fornecedores, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FornecedorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)