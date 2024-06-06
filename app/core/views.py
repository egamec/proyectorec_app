from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def house(request):
    return render(request, 'dashboard.html')


def facial(request):
    return render(request, 'facial.html')


def clasificacion(request):
    return render(request, 'clasificacion.html')


def informes(request):
    return render(request, 'informes.html')


def recetas(request):
    return render(request, 'recetas.html')


def recomendacion(request):
    return render(request, 'recomendacion_nutri.html')

