from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from clientes.models import Proveedores
from fracciones.models import Fraccion
from .forms import ProductoForm

def lista_productos(request):
    query = request.GET.get('q', '')
    page = int(request.GET.get('page', 1))
    page_size = 20
    offset = (page - 1) * page_size

    if request.method == 'POST':
        prod_id = request.POST.get('producto_id')
        if prod_id:
            producto = get_object_or_404(Producto, id_prod=prod_id)
            form = ProductoForm(request.POST, instance=producto)
        else:
            form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos:Productos')  # Cambia por el nombre real de la ruta
    else:
        form = ProductoForm()

    productos = Producto.objects.select_related('id_prov', 'id_frcc').filter(codigo__icontains=query)[offset:offset + page_size]
    total = Producto.objects.filter(codigo__icontains=query).count()

    return render(request, 'productos.html', {
        'productos': productos,
        'form': form,
        'query': query,
        'page': page,
        'total_pages': (total + page_size - 1) // page_size
    })
