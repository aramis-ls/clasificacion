from django import forms

class clasificacion(forms.Form):
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

class clasificar(forms.Form):
    cod = forms.CharField(label='Columna Código de Producto')
    prov = forms.CharField(label='Columna Proveedor')
    frcc = forms.CharField(label='Columna Fracción')
    pe = forms.CharField(label='Columna Precio Estimado')
    arancel = forms.CharField(label='Columna Arancel')
    fila = forms.IntegerField(label='Fila de inicio de los datos', min_value=1)
    archivo = forms.FileField(label='Archivo Excel')
