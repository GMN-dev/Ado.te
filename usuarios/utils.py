from django.contrib import messages


def isFormRegisterValid(request, nome, email, senha, confirmar_senha):
    if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or len(confirmar_senha.strip()) == 0:
        messages.add_message(request, messages.constants.ERROR, 'Preencha os campos devidamente')
        return False
    else:
        return True


def isPasswwordEquals(request, senha, confirmar_senha):
    if senha != confirmar_senha:
        messages.add_message(request, messages.constants.ERROR, 'As senha não conferem')
        return False
    else:
        return True