import uuid
from django.db import models

class Proveedores(models.Model): #tabla de clientes o proveedores
    id_prov = models.UUIDField(primary_key=True, default=uuid.uuid4, editable= False)
    nombre_prov = models.CharField(max_length=100, blank=True, null=True) #nombre del cliente/proveedor
    taxid = models.CharField(unique=True, max_length=15, blank=False, null= False) #identificador del cliente, taxid, o RFC del cliente/proveedor
    domicilio = models.CharField(max_length=300, blank=True, null=True) # domicilio del cliente/proveedor

    class Meta:
        managed=False
        db_table = 'proveedores'
