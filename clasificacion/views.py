from django.http import HttpResponse
import pandas as pd 
from django.shortcuts import render
from .forms import ExcelUploadForm
from productos.models import Producto

def clasificacion(request):
    lista_encontrados = []
    lista_faltantes = []

    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            columna=form.cleaned_data['clve_prod']
            fila=form.cleaned_data.get('fila'-1) or 0                                
            df = pd.read_excel(request.FILES['archivo'], fila)

            if columna not in df.columns:  
                return HttpResponse("No se encontro la columna especificada")
            
            claves_excel = df[columna].dropna().astype(str).unique()

            productos = Producto.objects.filter(clave__inx=claves_excel)
            claves_db = set(productos.values_list('clave', flat=True))

            for producto in productos:
                lista_encontrados.append({
                    'clave': producto.clave,
                    'fraccion': producto.fraccion_arancelaria,
                    'regulaciones': producto.regulaciones,
                    'precio': producto.precio_estimado
                })

            faltantes = set(claves_excel) - claves_db
            for clave in faltantes:
                lista_faltantes.append(clave)
    else:
        form = ExcelUploadForm()

    return render(request, 'clasificar.html', {
        'form': form,
        'lista_encontrados': lista_encontrados,
        'lista_faltantes': lista_faltantes
    })
