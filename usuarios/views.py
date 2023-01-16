from django.shortcuts import render,redirect
from .utils import isFormRegisterValid, isPasswwordEquals
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

# Create your views here.
def cadastro(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/divulgar/novo_pet/')
        else:
            return render(request, 'cadastro.html')

    if request.method == "POST":
        nome, email, senha, conf_senha = request.POST.get('nome'), request.POST.get('email'), request.POST.get('senha'), request.POST.get('confirmar_senha')
        if isFormRegisterValid(request, nome, email, senha, conf_senha) and isPasswwordEquals(request, senha, conf_senha):
            try:
                user = User.objects.create_user(username=nome, email=email, password=senha)
                messages.add_message(request, messages.constants.SUCCESS, 'Cadastro realizado com sucesso!')

            except:
                messages.add_message(request, messages.constants.ERROR, 'Erro no cadastro, contate o suporte ou o administrador.')
        
        return redirect('cadastro')


def login_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/divulgar/novo_pet/')
        else:
            return render(request, "login.html")
    
    elif request.method == "POST":
        username = request.POST.get('nome')
        password = request.POST.get('senha')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/divulgar/novo_pet')
        else:
            messages.add_message(request, messages.constants.ERROR, 'Usuário ou senha inválidos')
            return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
        

def temp(request):
    user = request.user.username
    return HttpResponse(f'{user}')
        

        
            
