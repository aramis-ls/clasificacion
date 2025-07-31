from django import forms
from .models import Productos, Proveedores, Fraccion

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['codigo', 'id_prov', 'id_frcc']
        labels = {
            'codigo': 'Código del producto',
            'id_prov': 'Proveedor',
            'id_frcc': 'Fracción'
        }
    