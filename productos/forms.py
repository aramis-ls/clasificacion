from django import forms
from .models import Producto
from fracciones.models import Fraccion
from clientes.models import Proveedores

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'id_prov', 'id_frcc']
        labels = {
            'codigo': 'Código del producto',
            'id_prov': 'Proveedor',
            'id_frcc': 'Fracción'
        }
    