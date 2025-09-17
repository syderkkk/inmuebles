from django.shortcuts import render
from .models import Propiedad

# Create your views here.

def listar_propiedades(request):
    propiedades = Propiedad.objects.all()

    return render(request, 'inmuebles/listar_inmuebles.html', {
        'propiedades': propiedades,
    })