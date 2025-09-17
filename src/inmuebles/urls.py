
from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar_propiedades, name="listar_propiedades"),
    path("crear/", views.crear_propiedad, name="crear_propiedad")
]