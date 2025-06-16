
from django.urls import path
from financeiro.views.fornecedor import FornecedorAPIView

urlpatterns = [
    path(
        'fornecedores/', 
        FornecedorAPIView.as_view(), 
        name='fornecedor-list-create'
    ),
    
    path(
        'fornecedores/<int:pk>/', 
        FornecedorAPIView.as_view(), 
        name='fornecedor-detail'
    ),
]