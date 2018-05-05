from django.db import models
from django.contrib.auth.models import User 
# from apps.personas.models import Personas
# Create your models here.
class Datos(models.Model):
    tipo_list = (
        ('entra', 'Entra'),
        ('sale', 'Sale'),
    )
    date_creation = models.DateField()
    tipo = models.CharField(max_length=255, choices=tipo_list)
    hora_ingreso = models.DateField()
    is_active = models.BooleanField(default=False)
    users = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    # personas = models.ManyToManyField(Personas)