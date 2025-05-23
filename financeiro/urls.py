from django.urls import path
from financeiro import views

urlpatterns = [
    path('fornecedores/', views.fornecedor_list),
]