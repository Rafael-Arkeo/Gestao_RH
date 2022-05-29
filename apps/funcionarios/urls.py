from django.urls import path
from .views import ListaFuncionario, UpdateFuncionario, DeleteFuncionario



urlpatterns = [
    path('', ListaFuncionario.as_view(), name='lista_funcionarios'),
    path('update/<int:pk>/', UpdateFuncionario.as_view(), name='update_funcionario'),
    path('delete/<int:pk>/', DeleteFuncionario.as_view(), name='delete_funcionario'),

]