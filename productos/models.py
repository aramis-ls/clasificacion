from django.db import models

from clientes.models import Proveedores
from fracciones.models import Fraccion

class Producto(models.Model):
    id_prod = models.AutoField(primary_key=True) # identificador de la tabla Producto
    codigo = models.CharField(max_length=20) # Codigo del producto, como service tag, o cualquier otro identificador (depende del proveedor)
    id_prov = models.ForeignKey(Proveedores, models.DO_NOTHING, db_column='id_prov', blank=True, null=True)  #identificador del proveedor (llave foranea)
    id_frcc = models.ForeignKey(Fraccion, models.DO_NOTHING, db_column='id_frcc') #fraccion arancelaria asociado (llave foranea)

    class Meta:
        managed=False
        db_table = 'producto'
        unique_together = (('codigo', 'id_prov', 'id_frcc'), ('codigo', 'id_prov'),) 
    #unique para que se ingrese solo un producto de un cliente        
    #otro para que a ese producto unico por cliente tenga una unica fraccion arancelaria