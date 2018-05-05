from django.shortcuts import render
from django.http import HttpResponse
from apps.datos.models import Datos
from apps.personas.models import Personas
import getpass
# import pwd
def index(request):
    p = Personas(
        nombre = "Carlos",
        apellido = "hh",
        identificacion = "098091",
        email = "xx@gmail.com"
    )
    p.save()
    dat = Datos(
        tipo = "entra",
        date_creation = "2018-05-05",
        hora_ingreso = "2018-05-05",
        # users = get_user()
    ) 
    dat.save()
    p.datos.add(dat)  
    p.save() 
    return HttpResponse("fin")

