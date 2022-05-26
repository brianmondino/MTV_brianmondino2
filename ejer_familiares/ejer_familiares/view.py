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
