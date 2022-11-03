from django.urls import path
from .views import CreateEmpresa


urlpatterns = [
    path('create/', CreateEmpresa.as_view(), name='create_empresa')
]