from django.shortcuts import render, HttpResponse

from carro.carro import Carro


# Create your views here.

def Inicio(request):
    carro=Carro(request)
    return render(request, "proyectoApp/Inicio.html")








