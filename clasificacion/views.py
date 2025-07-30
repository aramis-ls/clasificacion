import os
from django.http import HttpResponse
import pandas as pd 
from django.shortcuts import render, redirect

from clasificador import settings
from .forms import clasificar
from productos.models import Producto
from fracciones.models import Fraccion
from clientes.models import Proveedores

def clasificacion(request):
    clasificados = []
    no_clasificados = []

    if request.method == 'POST':
        form = clasificar(request.POST, request.FILES)
        if form.is_valid():
            archivo=form.cleaned_data['archivo']
            product=form.cleaned_data['clve_prod']
            proveed=form.cleaned_data['proveedor']
            fila=form.cleaned_data['fila']
            df = pd.read_excel(archivo, header=fila-1)

            #valid
            for index, row in df.iterrows():
                codigo = str(row[product]).strip()
                nombre_prov = str(row[proveed]).strip()

                try:
                    proveedor = Proveedores.objects.get(nombre_prov__iexact=nombre_prov)
                    producto = Producto.objects.get(codigo=codigo, id_prov=proveedor)

                    fraccion = producto.id_frcc
                    clasificados.append({
                        'clave': codigo,
                        'proveedor': proveedor.nombre_prov,
                        'fraccion': fraccion.nombre_frcc,
                        'pe': fraccion.pe,
                        'arancel': fraccion.arancel,
                    })
                except (Proveedores.DoesNotExist, Producto.DoesNotExist, AttributeError):
                    no_clasificados.append({
                        'clave': codigo,
                        'proveedor': nombre_prov
                    })

            # Convertir a DataFrame
            df_clasificados = pd.DataFrame(clasificados)
            df_no_clasificados = pd.DataFrame(no_clasificados)

            # Guardar archivos
            ruta_clasificados = os.path.join(settings.MEDIA_ROOT, 'clasificados.xlsx')
            ruta_no_clasificados = os.path.join(settings.MEDIA_ROOT, 'no_clasificados.xlsx')

            df_clasificados.to_excel(ruta_clasificados, index=False)
            df_no_clasificados.to_excel(ruta_no_clasificados, index=False)

            return render(request, 'clasificado.html', {
                'archivo_clasificados': 'clasificados.xlsx',
                'archivo_no_clasificados': 'no_clasificados.xlsx'
            })

    else:
        form = clasificar()

    return render(request, 'clasificar.html', {'form': form,})
