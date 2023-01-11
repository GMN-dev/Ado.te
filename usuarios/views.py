from django.shortcuts import render,redirect
from .utils import isFormRegisterValid, isPasswwordEquals
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')

    if request.method == "POST":
        nome, email, senha, conf_senha = request.POST.get('nome'), request.POST.get('email'), request.POST.get('senha'), request.POST.get('confirmar_senha')
        if isFormRegisterValid(request, nome, email, senha, conf_senha) and isPasswwordEquals(request, senha, conf_senha):
            return HttpResponse(request, 'Acesso concedido')
        else:
            return redirect('cadastro')

            
