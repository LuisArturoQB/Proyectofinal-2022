from django.shortcuts import render
from .models import Producto

# Create your views here.

def compra(request):
    productos=Producto.objects.all()
    return render(request, "compra/compra.html", {"productos":productos})
