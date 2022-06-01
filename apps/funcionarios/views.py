from django.views.generic import\
(
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
)
from .models import Funcionario
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class ListaFuncionario(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class UpdateFuncionario(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']


class DeleteFuncionario(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('lista_funcionarios')



class CreateFuncionario(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']
    success_url = reverse_lazy('lista_funcionarios')

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create_user(username=username)
        funcionario.save()
        return super(CreateFuncionario, self).form_valid(form)

