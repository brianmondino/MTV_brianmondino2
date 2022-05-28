from django.shortcuts import render
from app_familia.models import miembros
# Create your views here.


def miembroos(request):
    fam_nuevo =miembros.objects.create(
        nombre = 'Brian', 
        apellido = 'Mondino', 
        dni = '34111222', 
        fecha_nac='18-10-88', 
        telefono ='478611111'
        )
    context = {'fam_nuevo':fam_nuevo}
    return render(request, 'tem_fam3.html', context = context)