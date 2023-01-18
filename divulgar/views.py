from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Tag, Raca
from django.contrib import messages
from .models import Pet, Tag
# Create your views here.


@login_required(login_url='/auth/login/')
def novo_pet(request):
    if request.method == 'GET':
        tags = Tag.objects.all()
        racas = Raca.objects.all()
        return render(request, 'novo_pet.html', {'tags':tags, 'racas':racas})
    
    if request.method == 'POST':
        foto = request.FILES.get('foto')
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        telefone = request.POST.get('telefone')
        tags_ = request.POST.getlist('tags')
        raca = request.POST.get('raca')

        try:
            pet = Pet.objects.create(
                usuario = request.user,
                foto = foto,
                nome = nome,
                descricao = descricao, 
                estado = estado,
                cidade = cidade ,
                telefone = telefone,
                raca_id = raca
            )

            pet.save()

            for i in tags_:
                tag = Tag.objects.get(id = i)
                pet.tags.add(tag)

            pet.save()

            messages.add_message(request, messages.constants.SUCCESS, 'Pet adicionado com sucesso!')
        except:
            messages.add_message(request, messages.constants.ERROR, 'Erro, contate o administrador!')

        return redirect('novo_pet')

@login_required(login_url='/auth/login/')
def seus_pets(request):
    if request.method == 'GET':
        meus_pets = Pet.objects.filter(usuario = request.user)
        return render(request, 'seus_pets.html', {'pets':meus_pets})