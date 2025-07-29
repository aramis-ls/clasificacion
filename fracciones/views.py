from django.shortcuts import render, redirect, get_object_or_404
from .forms import FraccionRegulacionForm
from .models import Fraccion, Regulaciones, FraccionRel
from django.db import transaction

def lista_fracciones(request):
    query = request.GET.get('q', '')
    page = int(request.GET.get('page', 1))
    page_size = 20
    offset = (page - 1) * page_size

    if request.method == 'POST':
        fracc_id = request.POST.get('fraccion_id')
        form = FraccionRegulacionForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                # Obtener o crear fracción
                if fracc_id:
                    fraccion = get_object_or_404(Fraccion, id_frcc=fracc_id)
                    fraccion.nombre_frcc = form.cleaned_data['nombre_frcc']
                    fraccion.desc_frcc = form.cleaned_data['desc_frcc']
                    fraccion.pe = form.cleaned_data['pe']
                    fraccion.arancel = form.cleaned_data['arancel']
                    fraccion.save()
                else:
                    fraccion = Fraccion.objects.create(
                        nombre_frcc=form.cleaned_data['nombre_frcc'],
                        desc_frcc=form.cleaned_data['desc_frcc'],
                        pe=form.cleaned_data['pe'],
                        arancel=form.cleaned_data['arancel']

                    )
                

                # Obtener o crear regulación
                regulacion, _ = Regulaciones.objects.get_or_create(
                    nombre_reg=form.cleaned_data['nombre_reg'],
                    defaults={'desc_reg': form.cleaned_data['desc_reg']}
                )

                # Crear relación
                if not FraccionRel.objects.filter(id_frcc=fraccion, id_reg=regulacion).exists():
                    FraccionRel.objects.create(id_frcc=fraccion, id_reg=regulacion)

            return redirect('fracciones:Fracciones')  # Reemplaza con tu nombre de URL
    else:
        form = FraccionRegulacionForm()

    relaciones = FraccionRel.objects.select_related('id_frcc', 'id_reg').filter(id_frcc__nombre_frcc__icontains=query)[offset:offset + page_size]
    total = FraccionRel.objects.select_related('id_frcc', 'id_reg').filter(id_frcc__nombre_frcc__icontains=query).count()

    return render(request, 'fracciones.html', {
        'relaciones': relaciones,
        'query': query,
        'page': page,
        'total_pages': (total + page_size - 1) // page_size,
        'form': form,

    })
