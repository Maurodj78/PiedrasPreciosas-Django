from django.shortcuts import render
from .models import Producto


# Create your views here.
def catalog(request):
    productos = Producto.objects.all()
    return render(request, "catalogo/catalogo.html", {"productos": productos})
