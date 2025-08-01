import os
from django.contrib import messages
from django.http import HttpResponse
import pandas as pd 
from django.shortcuts import render, redirect

from clasificador import settings
from .forms import clasificar, clasificacion
from productos.models import Producto
from fracciones.models import Fraccion
from clientes.models import Proveedores

def clasificacion_excel(request):
    clasificados = []
    no_clasificados = []

    if request.method == 'POST':
        form = clasificacion(request.POST, request.FILES)
        if form.is_valid():
            archivo=form.cleaned_data['archivo']
            product=form.cleaned_data['clve_prod']
            proveed=form.cleaned_data['proveedor']
            fila=form.cleaned_data['fila']

            try:
                df = pd.read_excel(archivo, dtype=str, skiprows=fila - 1)
                if product not in df.columns or proveed not in df.columns:
                    raise ValueError("Columnas no encontradas")
            except Exception as e:
                messages.error(request, f"Error al procesar archivo: {str(e)}")
                return render(request, 'clasificacion.html', {'form': form})



            df = pd.read_excel(archivo, header=fila-1)

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
        form = clasificacion()

    return render(request, 'clasificacion.html', {'form': form,})

def clasificar_excel(request):
    if request.method == 'POST':
        form = clasificar(request.POST, request.FILES)
        if form.is_valid():
            archivo = form.cleaned_data['archivo']
            fila_inicio = form.cleaned_data['fila']
            col_codigo = form.cleaned_data['cod']
            col_prov = form.cleaned_data['prov']
            col_frac = form.cleaned_data['frcc']
            col_pe = form.cleaned_data['pe']
            col_arancel = form.cleaned_data['arancel']
            col_taxid=form.cleaned_data['tax_id']

            try:
                df = pd.read_excel(archivo, dtype=str, skiprows=fila_inicio - 1)

                # Validar columnas
                for col in [col_codigo, col_prov, col_frac, col_pe, col_arancel, col_taxid]:
                    if col not in df.columns:
                        messages.error(request, f"Columna '{col}' no encontrada.")
                        return render(request, 'clasificar.html', {'form': form})

                for _, row in df.iterrows():
                    codigo = row[col_codigo].strip()
                    proveedor_nombre = row[col_prov].strip()
                    tax_id=row[col_taxid].strip()
                    fraccion_nombre = row[col_frac].strip()
                    pe = row[col_pe].strip()
                    arancel = row[col_arancel].strip()

                    # Insertar o recuperar proveedor
                    proveedor, _ = Proveedores.objects.get_or_create(nombre_prov=proveedor_nombre,
                        defaults={'tax_id':tax_id})

                    # Insertar o recuperar fracción
                    
                    fraccion, _ =Fraccion.objects.get_or_create(
                        nombre_frcc=fraccion_nombre,
                        defaults={'desc_frcc': '', 'pe': pe, 'arancel': arancel}
                    )

                    # Insertar producto si no existe
                    Producto.objects.get_or_create(
                        codigo=codigo,
                        id_prov=proveedor,
                        defaults={'id_frcc': fraccion}
                    )

                messages.success(request, "Datos cargados correctamente.")
                return redirect('/clasificacion/clasificado/clasificar')
            except Exception as e:
                messages.error(request, f"Error al procesar archivo: {str(e)}")
    else:
        form = clasificar()

    return render(request, 'clasificar.html', {'form': form})
