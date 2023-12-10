from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render(request, "core/index.html")


def catalog(request):
    return render(request, "core/catalogo.html")


def promociones(request):
    return render(request, "core/promociones.html")


def contact(request):
    return render(request, "core/contacto.html")
