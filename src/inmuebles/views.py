from django.shortcuts import render, redirect
from .models import Propiedad
from .forms import PropiedadForm

# Create your views here.

def listar_propiedades(request):
    propiedades = Propiedad.objects.all()

    return render(request, 'inmuebles/listar_inmuebles.html', {
        'propiedades': propiedades,
    })


def crear_propiedad(request):
    if request.method == 'POST':
        form = PropiedadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_propiedades')
    else:
        form = PropiedadForm()
    return render(request, 'inmuebles/crear_inmuebles.html', {'form': form})