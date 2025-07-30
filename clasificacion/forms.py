from django import forms

class clasificar(forms.Form):
    clve_prod= forms.CharField(
        label="¿Cual es la columna de las claves de productos?",
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Ej: Producto, claves, etc'})

    )
    proveedor= forms.CharField(
        label="¿Cual es la columna del proveedor?",
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Ej: cliente, proveedor, etc'})

    )
    fila=forms.IntegerField(
        label="¿Donde empieza la tabla?",
        required=False,
        min_value=1,
        widget=forms.NumberInput(attrs={
        'placeholder':"Ej: 1, 3, 5, etc (1 si no se anota)"})
    )
    archivo = forms.FileField()
