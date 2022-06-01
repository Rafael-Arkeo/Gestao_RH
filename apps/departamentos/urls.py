from django.urls import path
from .views import\
    (
    DepartamentoView, DepartamentoUpdateView,
    DepartamentoDeleteView, DepartamentoCreateView

)



urlpatterns = [
    path('', DepartamentoView.as_view(), name='lista_departamentos'),
    path('update/<int:pk>/', DepartamentoUpdateView.as_view(), name='update_departamento'),
    path('delete/<int:pk>/', DepartamentoDeleteView.as_view(), name='delete_departamento'),
    path('create', DepartamentoCreateView.as_view(), name='create_departamento'),


]