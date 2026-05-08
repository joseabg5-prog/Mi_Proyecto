from django.shortcuts import render, get_object_or_404
from .models import Coffee

# Vista de la página principal
def home(request):
    mis_cafes = Coffee.objects.all()
    return render(request, 'home.html', {'lista_cafes': mis_cafes})

# Nueva vista para el detalle del servicio
def detalle_servicio(request, pk):
    # Buscamos el servicio por su ID (pk) o lanzamos error 404 si no existe
    servicio = get_object_or_404(Coffee, pk=pk)
    return render(request, 'detalle.html', {'servicio': servicio})
