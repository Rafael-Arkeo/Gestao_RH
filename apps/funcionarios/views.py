from django.views.generic import ListView, UpdateView
from .models import Funcionario

class ListaFuncionario(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)

class UpdateFuncionario(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']


