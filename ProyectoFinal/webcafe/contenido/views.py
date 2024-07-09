from django.shortcuts import render
from .models import Receta


# Create your views here.

def db(request):
    rexetas = Receta.objects.all()
    return render(request, "contenido/db.html", {'rexetas':rexetas})
