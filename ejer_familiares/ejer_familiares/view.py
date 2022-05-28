from django.http import HttpResponse
from django.shortcuts import render




def saludo(request):
	return HttpResponse('El mondi saluda')

def template1_test (request):
    return render(request, 'tem_fam.html', context = {})

def template2_test(request):
    context = {
        'nombre': 'Brian',
        'apellido':'Mondino'
    }
    return render(request, 'tem_fam2.html', context = context)

def temp3_entrega(request):
    context = {
        'nombre': 'Brian',
        'apellido':'Mondino',
        'dni':'11111111',
        'fecha_nac':'18/10/1988',
        'telefono':'4786-4444'
    }
    return render(request, 'tem_fam3.html', context = context)

