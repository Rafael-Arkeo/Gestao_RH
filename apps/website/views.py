from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from apps.funcionarios.models import Funcionario

@login_required
def home(request):
    """data = {}
    data['usuario'] = request.user
    return render(request, 'website/index.html', data)"""""
    return HttpResponse('olá')
