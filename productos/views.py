from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from .models import Producto
from .forms import ProductoForm
from clientes.models import Proveedores
from fracciones.models import Fraccion

def lista_productos(request):
    query = request.GET.get('q', '')
    page = int(request.GET.get('page', 1))
    page_size = 20
    offset = (page - 1) * page_size

    if request.method == 'POST':
        prod_id = request.POST.get('producto_id')
        form = ProductoForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                if prod_id:
                    producto = get_object_or_404(Producto, id_prod=prod_id)
                    producto.codigo = form.cleaned_data['codigo']
                    producto.id_prov = form.cleaned_data['id_prov']
                    producto.id_frcc = form.cleaned_data['id_frcc']
                    producto.save()
                else:
                    Producto.objects.create(
                        codigo=form.cleaned_data['codigo'],
                        id_prov=form.cleaned_data['id_prov'],
                        id_frcc=form.cleaned_data['id_frcc']
                    )
            return redirect('productos:Productos')  # Asegúrate de que esta URL esté registrada
    else:
        form = ProductoForm()

    productos = Producto.objects.select_related('id_prov', 'id_frcc').filter(codigo__icontains=query)[offset:offset + page_size]
    total = Producto.objects.filter(codigo__icontains=query).count()

    return render(request, 'productos.html', {
        'productos': productos,
        'query': query,
        'page': page,
        'total_pages': (total + page_size - 1) // page_size,
        'form': form,
    })
