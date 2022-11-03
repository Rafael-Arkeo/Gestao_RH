from django.views.generic import CreateView
from django.http import HttpResponse
from .models import Empresa


class CreateEmpresa(CreateView):
    model = Empresa
    fields = ['nome']


    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return HttpResponse('ok')
