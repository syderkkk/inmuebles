from django.db import models

# Create your models here.
class Propiedad(models.Model):
    direccion = models.CharField(max_length = 150)
    precio = models.CharField(max_length = 150)
    tipo = models.CharField(max_length = 150)