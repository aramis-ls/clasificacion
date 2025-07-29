from django import forms
from .models import Fraccion, Regulaciones

class FraccionRegulacionForm(forms.Form):
    nombre_frcc = forms.CharField(label='Fracción')
    desc_frcc = forms.CharField(label='Descripción Fracción', widget=forms.Textarea)
    pe = forms.DecimalField(label='PE')
    arancel = forms.DecimalField(label='Arancel')

    nombre_reg = forms.CharField(label='Regulación', max_length=100)
    desc_reg = forms.CharField(label='Descripción Regulación', widget=forms.Textarea)
