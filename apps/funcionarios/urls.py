from django.urls import path
from .views import ListaFuncionario, UpdateFuncionario, DeleteFuncionario,CreateFuncionario



urlpatterns = [
    path('', ListaFuncionario.as_view(), name='lista_funcionarios'),
    path('update/<int:pk>/', UpdateFuncionario.as_view(), name='update_funcionario'),
    path('delete/<int:pk>/', DeleteFuncionario.as_view(), name='delete_funcionario'),
    path('create/', CreateFuncionario.as_view(), name='create_funcionario'),

]