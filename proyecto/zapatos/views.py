from django.shortcuts import render
from zapatos.models import zapatos

# Create your views here.

def Zapatos(request):
    Zapatos=zapatos.objects.all()
    return render(request, "zapatos/Zapatos.html", {"Zapatos": Zapatos})
