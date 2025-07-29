from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def inicio(request):
    funciones = [
        {"nombre": "Clasificar", "url": "/clasificacion/", 'descripcion': 'Introducir excel para realizar una busqueda'},
        {"nombre": "Fracciones", "url": "/fracciones/", 'descripcion': 'Ver las fracciones existentes'},
        {"nombre": "Productos", "url": "/productos/", 'descripcion': 'Muestra los productos clasificados con anterioridad junto con su fraccion'},
        {"nombre": "Clientes", "url": "/clientes/", 'descripcion': 'Clientes con los que se ha trabajado'},
        
    ]
    return render(request, 'inicio.html', {
        "funciones": funciones
        })
