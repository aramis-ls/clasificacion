from django import forms
from clientes.models import Proveedores

class NuevoProv(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = ['nombre_prov', 'taxid', 'domicilio']
        widgets = {
            'nombre_prov': forms.TextInput(attrs={'placeholder': 'Nombre del cliente'}),
            'taxid': forms.TextInput(attrs={'placeholder': 'RFC o Tax ID'}),
            'domicilio': forms.Textarea(attrs={'placeholder': 'Dirección completa', 'rows': 3}),
        }
