from django.db import models
from ConfiguracionApp.models import *
from SolicitudesApp.models import *

# Create your models here.

class PresupuestoDatoGen(models.Model):
    Id= models.AutoField(primary_key=True)
    Fecha= models.DateField(null=False)
    MejoraReal= models.CharField(max_length=200)
    DiasEstiCon= models.CharField(max_length=10)
    IdSolicitud=models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='PresupuestoDatoGen'
        verbose_name_plural='PresupuestoDatoGens'
        db_table= 'PresupuestoDatoGen'
        

class PresupuestoMate(models.Model):
    Id= models.AutoField(primary_key=True)
    PrecioUnit= models.DecimalField(decimal_places=2, max_digits=15)
    Cantidad= models.DecimalField(decimal_places=2, max_digits=15)
    SubTota= models.DecimalField(decimal_places=2, max_digits=20)
    IdMateriales=models.ForeignKey(Materiales, on_delete=models.CASCADE)
    IdPresupuestoDatoGen=models.ForeignKey(PresupuestoDatoGen, on_delete=models.CASCADE)

    class Meta:
        verbose_name='PresupuestoMate'
        verbose_name_plural='PresupuestoMates'
        db_table= 'PresupuestoMate'
        
class PresupuestoManoObr(models.Model):
    Id= models.AutoField(primary_key=True)
    Descripcion= models.CharField(max_length=100)
    Unidad= models.CharField(max_length=10)
    PrecioUnit= models.DecimalField(decimal_places=2, max_digits=15)
    Cantidad= models.DecimalField(decimal_places=2, max_digits=15)
    SubTota= models.DecimalField(decimal_places=2, max_digits=20)
    IdPresupuestoDatoGen=models.ForeignKey(PresupuestoDatoGen, on_delete=models.CASCADE)

    class Meta:
        verbose_name='PresupuestoManoObr'
        verbose_name_plural='PresupuestoManoObrs'
        db_table= 'PresupuestoManoObr'

class PresupuestoOtro(models.Model):
    Id= models.AutoField(primary_key=True)
    Descripcion= models.CharField(max_length=100)
    Unidad= models.CharField(max_length=10)
    PrecioUnit= models.DecimalField(decimal_places=2, max_digits=15)
    Cantidad= models.DecimalField(decimal_places=2, max_digits=15)
    SubTota= models.DecimalField(decimal_places=2, max_digits=20)
    IdPresupuestoDatoGen=models.ForeignKey(PresupuestoDatoGen, on_delete=models.CASCADE)

    class Meta:
        verbose_name='PresupuestoOtro'
        verbose_name_plural='PresupuestoOtros'
        db_table= 'PresupuestoOtro'

class Presupuesto(models.Model):
    Id= models.AutoField(primary_key=True)
    SubTota= models.DecimalField(decimal_places=2, max_digits=15)
    AsistenciaTecn= models.DecimalField(decimal_places=2, max_digits=15)
    ComisionPorOto= models.DecimalField(decimal_places=2, max_digits=15)
    ConsultaBuroCre= models.DecimalField(decimal_places=2, max_digits=15)
    CancelarSaldPen= models.DecimalField(decimal_places=2, max_digits=15)
    PrimeraCuot= models.DecimalField(decimal_places=2, max_digits=15)
    Total= models.DecimalField(decimal_places=2, max_digits=20)
    Notas= models.CharField(max_length=500)
    IdPresupuestoDatoGen=models.ForeignKey(PresupuestoDatoGen, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Presupuesto'
        verbose_name_plural='Presupuestos'
        db_table= 'Presupuesto'


