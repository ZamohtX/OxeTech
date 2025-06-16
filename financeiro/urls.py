from django.urls import path
from financeiro.views.fornecedor import FornecedorViewSet

urlpatterns = [
    # Fornecedores
    path('fornecedores/', FornecedorViewSet.as_view(), name='fornecedor-list'),
    path('fornecedores/<int:pk>/', FornecedorViewSet.as_view(), name='fornecedor-detail'),
]
