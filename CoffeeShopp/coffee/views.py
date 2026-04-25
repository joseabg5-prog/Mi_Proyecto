from django.shortcuts import render
from django.http import HttpResponse
from .models import Coffee


def home(request):
    # 1. Guardamos todos los registros en una variable (en plural mejor)
    mis_cafes = Coffee.objects.all() 
    
    # 2. Pasamos ESA variable al diccionario del contexto
    return render(request, 'home.html', {'lista_cafes': mis_cafes})
