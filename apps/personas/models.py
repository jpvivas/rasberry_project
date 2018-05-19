from django.db import models
from apps.datos.models import Datos

# Create your models here.
class Personas(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    identificacion = models.CharField(max_length=255)
    email= models.EmailField(max_length=255)
    is_active = models.BooleanField(default=False)
    datos = models.ManyToManyField(Datos)
    tarjeta_uid = models.CharField(max_length=255)

