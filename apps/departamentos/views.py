from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import\
    (
     ListView,
     UpdateView,
     DeleteView,
     CreateView
     )

from apps.departamentos.models import Departamento


class DepartamentoView(ListView):
    model = Departamento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)


class DepartamentoUpdateView(UpdateView):
    model = Departamento
    fields = ['nome']

class DepartamentoDeleteView(DeleteView):
    model = Departamento
    success_url = reverse_lazy('lista_departamentos')



class DepartamentoCreateView(CreateView):
    model = Departamento
    fields = ['nome']

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentoCreateView, self).form_valid(form)