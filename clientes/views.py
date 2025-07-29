from django.shortcuts import get_object_or_404, redirect, render

from .forms import NuevoProv
from clientes.models import Proveedores


def lista_clientes(request):
    query = request.GET.get('q', '')
    page = int(request.GET.get('page', 1))
    page_size = 20
    offset = (page - 1) * page_size

    if request.method == 'POST':
        cliente_id=request.POST.get('cliente_id')
        if cliente_id:
            cliente=get_object_or_404(Proveedores, taxid=cliente_id)
            form=NuevoProv(request.POST,instance=cliente)
        else:
            form = NuevoProv(request.POST)
            
        if form.is_valid():
            form.save()
            return redirect('clientes:Clientes')
    else:
        form = NuevoProv()

    proveedores = Proveedores.objects.filter(taxid__icontains=query)[offset:offset + page_size]
    total = Proveedores.objects.filter(taxid__icontains=query).count()

    return render(request, 'clientes.html', {
        'proveedores': proveedores,
        'query': query,
        'page': page,
        'total_pages': (total + page_size - 1) // page_size,
        'form': form
    })
