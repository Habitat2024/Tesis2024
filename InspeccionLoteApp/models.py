from django.db import models
from ConfiguracionApp.models import *
from SolicitudesApp.models import *

# Create your models here.
class InspeccionLote(models.Model):
    Id= models.AutoField(primary_key=True)
    Fecha= models.DateField(null=False)
    Hora= models.CharField(max_length=15)
    TelefonoPrim= models.CharField(max_length=10)
    TelefonoSegu= models.CharField(max_length=10)
    TerceraEdad= models.CharField(max_length=10)
    Adultos= models.CharField(max_length=10)
    Ninos= models.CharField(max_length=10)
    PersonaDisc= models.CharField(max_length=10)
    PropietarioTerr= models.CharField(max_length=100)
    Latitud= models.CharField(max_length=100)
    Longitud= models.CharField(max_length=100)
    Inmueble= models.CharField(max_length=10)
    ExisteOtraViv= models.CharField(max_length=5)
    TerrenoAgri= models.CharField(max_length=5)
    AnchoConsViv= models.CharField(max_length=15)
    LargoConsViv= models.CharField(max_length=15)
    AreaConsViv= models.CharField(max_length=15)
    AnchoAmplFut= models.CharField(max_length=15)
    LargoAmplFut= models.CharField(max_length=15)
    AreaAmplFut= models.CharField(max_length=15)
    IdSolicitud= models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='InspeccionLote'
        verbose_name_plural='InspeccionLotes'
        db_table= 'InspeccionLote'


class InspeccionLoteConInfSanSerRie(models.Model):
    Id= models.AutoField(primary_key=True)
    IdInfraestructura=models.ForeignKey(Infraestructura, on_delete=models.CASCADE)
    Existe= models.CharField(max_length=5)
    IdInspeccionLote=models.ForeignKey(InspeccionLote, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='InspeccionLoteConInfSanSerRie'
        verbose_name_plural='InspeccionLoteConInfSanSerRies'
        db_table= 'InspeccionLoteConInfSanSerRie'

class RiesgosInspLot(models.Model):
    Id= models.AutoField(primary_key=True)
    DistanciaTalu= models.CharField(max_length=15)
    DistanciaRiosCer= models.CharField(max_length=15)
    DistanciaLadeCer= models.CharField(max_length=15)
    DistanciaTorrAnt= models.CharField(max_length=15)
    IdInspeccionLote=models.ForeignKey(InspeccionLote, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='RiesgosInspLot'
        verbose_name_plural='RiesgosInspLots'
        db_table= 'RiesgosInspLot'
    
class ComentariosObseInsLot(models.Model):
    Id= models.AutoField(primary_key=True)
    Comentarios= models.CharField(max_length=400)
    Observaciones= models.CharField(max_length=400)
    IdInspeccionLote=models.ForeignKey(InspeccionLote, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='ComentariosObseInsLot'
        verbose_name_plural='ComentariosObseInsLots'
        db_table= 'ComentariosObseInsLot'

class ViasAcceInsLot(models.Model):
    Id= models.AutoField(primary_key=True)
    TipoVias= models.CharField(max_length=35)
    IdInspeccionLote=models.ForeignKey(InspeccionLote, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='ViasAcceInsLot'
        verbose_name_plural='ViasAcceInsLots'
        db_table= 'ViasAcceInsLot'  
        
class FactibilidadInsLot(models.Model):
    Id= models.AutoField(primary_key=True)
    Detalle= models.CharField(max_length=300)
    IdInspeccionLote=models.ForeignKey(InspeccionLote, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='FactibilidadInsLot'
        verbose_name_plural='FactibilidadInsLots'
        db_table= 'FactibilidadInsLot'

class DescripcionProyInsLot(models.Model):
    Id= models.AutoField(primary_key=True)
    ModeloViviCon= models.CharField(max_length=30)
    SolucionSaniPro= models.CharField(max_length=300)
    ObrasAdicCon= models.CharField(max_length=300)
    ObservacionesTecn= models.CharField(max_length=400)
    ActividadRespFia= models.CharField(max_length=500)
    IdInspeccionLote=models.ForeignKey(InspeccionLote, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='DescripcionProyInsLot'
        verbose_name_plural='DescripcionProyInsLots'
        db_table= 'DescripcionProyInsLot'

class ResponsabilidadSoliInsLot(models.Model):
    Id= models.AutoField(primary_key=True)
    MojonesLote= models.CharField(max_length=5)
    LinderosLote= models.CharField(max_length=5)
    ResguardoMate= models.CharField(max_length=5)
    AuxiliaresCons= models.CharField(max_length=5)
    AguaPota= models.CharField(max_length=5)
    EnergiaElec= models.CharField(max_length=5)
    IdInspeccionLote=models.ForeignKey(InspeccionLote, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='ResponsabilidadSoliInsLot'
        verbose_name_plural='ResponsabilidadSoliInsLots'
        db_table= 'ResponsabilidadSoliInsLot'

# para primera inspección
class PrimeraInspLot(models.Model):
    Id= models.AutoField(primary_key=True)
    NumeroInsp= models.CharField(max_length=25)
    Fecha= models.DateField(null=False)
    Esquema= models.FileField(upload_to = "documentos/", blank=True)
    Ubicacion = models.FileField(upload_to="documentos/", blank=True)
    IdInspeccionLote= models.ForeignKey(InspeccionLote, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='PrimeraInspLot'
        verbose_name_plural='PrimeraInspLots'
        db_table= 'PrimeraInspLot'

class ImagenPrimInsLot(models.Model):
    Id= models.AutoField(primary_key=True)
    ReporteFoto= models.FileField(upload_to="documentos/", blank=True) 
    IdPrimeraInspLot= models.ForeignKey(PrimeraInspLot, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='ImagenPrimInsLot'
        verbose_name_plural='ImagenPrimInsLots'
        db_table= 'ImagenPrimInsLot'

