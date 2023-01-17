from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Tag, Raca

# Create your views here.
@login_required(redirect_field_name='/auth/login/')
def novo_pet(request):
    if request.method == 'GET':
        tags = Tag.objects.all()
        racas = Raca.objects.all()
        return render(request, 'novo_pet.html', {'tags':tags, 'racas':racas})
        


