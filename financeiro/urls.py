from django.urls import path
from financeiro import views

urlpatterns = [
    path('fornecedores/', views.fornecedor_list),
    path('fornecedor/<int:pk>/', views.fornecedor_detail),
    path('cidades/', views.cidade_list),
    path('cidades/<int:pk>/', views.cidade_detail),
    path('estados/', views.estado_list),
    path('estados/<int:pk>/', views.estado_detail)
]