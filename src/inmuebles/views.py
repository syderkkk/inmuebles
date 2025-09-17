from django.shortcuts import render
from .models import Propiedad

# Create your views here.

def listar_propiedades():
    propiedades = Propiedad.objects.all()
    return render("inmuebles/listar_inmuebles", propiedades)