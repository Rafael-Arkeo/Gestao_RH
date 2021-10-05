from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.funcionarios.models import Funcionario


def home(request):
    data = {}
    data['usuario'] = request.user
    return render(request, 'website/index.html', data)
