import uuid
from django.db import models

class Fraccion(models.Model): #tabla de fracciones
    id_frcc = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre_frcc = models.IntegerField(blank=False, null=False, unique=True) #fraccion arancelaria
    desc_frcc = models.CharField(max_length=200, blank=True, null=True) #descripcion de la fraccion
    pe = models.FloatField(blank=True, null=True) #precio estimado del producto (si aplica)
    arancel = models.IntegerField(blank=True, null=True) #arancel que se debe pagar (si aplica)

    class Meta:
        managed=False
        db_table = 'fraccion'
    def __str__(self):
        return str(self.nombre_frcc)
    


class Regulaciones(models.Model): # tabla de regulaciones 
    id_reg = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    nombre_reg = models.CharField(blank=False, null=False, max_length=15, unique=True) #regulacion a la que se le asocia la fraccion
    desc_reg = models.CharField(max_length=200, blank=True, null=True) #descripcion de la regulacion 

    class Meta:
        managed=False
        db_table = 'regulaciones'
    def __str__(self):
        return self.nombre_reg 

class FraccionRel(models.Model): #tabla intermedia de relacion entre regulaciones y fracciones 
    id_f_r = models.AutoField(primary_key=True) #identificador de la tabla
    id_reg = models.ForeignKey(Regulaciones, models.DO_NOTHING, db_column='id_reg', blank=False, null=True) #identificador de regulaciones (llave foranea)
    id_frcc = models.ForeignKey(Fraccion, models.DO_NOTHING, db_column='id_frcc', blank=False, null=True) #idnetificador de fracciones (llave foranea)
    class Meta:
        managed=False
        db_table = 'fraccion_rel'
        unique_together = (('id_frcc', 'id_reg'),) #unico entre fracciones y regulaciones
