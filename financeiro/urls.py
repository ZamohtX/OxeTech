
from django.urls import path
from financeiro.views.fornecedor import FornecedorAPIView
from financeiro.views.lancamento import LancamentoAPIView
from financeiro.views.forma_pagamento import FormaPagamentoAPIView
from financeiro.views.categoria import CategoriaAPIView
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

    path(
        'lancamentos/', 
        LancamentoAPIView.as_view(),
    ),
    path(
        'lancamentos/<int:pk>', LancamentoAPIView.as_view()
    ),
    path(
        'forma_pagamento/', FormaPagamentoAPIView.as_view()
    ),
    path(
        'forma_pagamento/<int:pk>', FormaPagamentoAPIView.as_view()
    ),
    path(
        'categoria/', CategoriaAPIView.as_view()
    ),
    path(
        'categoria/<int:pk>', CategoriaAPIView.as_view()
    )
]