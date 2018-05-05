from django.db import models
from apps.personas.models import Personas
# Create your models here.
class Fotos(models.Model):
    ruta = models.CharField(max_length=255)
    observaciones = models.TextField(max_length=255)
    is_active = models.BooleanField(default=False)
    personas = models.ForeignKey(Personas, null=True, blank=True, on_delete=models.CASCADE)