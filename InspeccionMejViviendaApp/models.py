from django.db import models
from ConfiguracionApp.models import *
from SolicitudesApp.models import *

# Create your models here.
class InspeccionMejo(models.Model):
    Id= models.AutoField(primary_key=True)
    Fecha= models.DateField(null=False)
    Hora= models.CharField(max_length=20)
    TelefonoPrim= models.CharField(max_length=10)
    TelefonoSegu= models.CharField(max_length=10)
    TerceraEdad= models.CharField(max_length=10)
    Adultos= models.CharField(max_length=10)
    Ninos= models.CharField(max_length=10)
    PersonaDisc= models.CharField(max_length=10)
    PropietarioInmu= models.CharField(max_length=100)
    ParentescoSoli= models.CharField(max_length=50)
    Latitud= models.CharField(max_length=100)
    Longitud= models.CharField(max_length=100)
    Inmueble= models.CharField(max_length=10)
    UsoActu= models.CharField(max_length=15)
    ExisteOtrViv= models.CharField(max_length=5)
    UsoActuOtrViv= models.CharField(max_length=15)
    ComentariosRelv= models.CharField(max_length=200)
    IdSolicitud= models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='InspeccionMejo'
        verbose_name_plural='InspeccionMejos'
        db_table= 'InspeccionMejo'

class InfraestructuraInmuInsMej(models.Model):
    Id= models.AutoField(primary_key=True)
    Existe= models.CharField(max_length=10)
    Estado= models.CharField(max_length=10)
    TipoSist= models.CharField(max_length=100)
    IdInfraestructura=models.ForeignKey(Infraestructura, on_delete=models.CASCADE)
    IdInspeccionMejo=models.ForeignKey(InspeccionMejo, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='InfraestructuraInmuInsMej'
        verbose_name_plural='InfraestructuraInmuInsMejs'
        db_table= 'InfraestructuraInmuInsMej'


class InspeccionMejoEspSerInfRie(models.Model):
    Id= models.AutoField(primary_key=True)
    Existe= models.CharField(max_length=10)
    IdInfraestructura=models.ForeignKey(Infraestructura, on_delete=models.CASCADE)
    IdInspeccionMejo=models.ForeignKey(InspeccionMejo, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='InspeccionMejoEspSerInfRie'
        verbose_name_plural='InspeccionMejoEspSerInfRies'
        db_table= 'InspeccionMejoEspSerInfRie'

class RiesgosInsMej(models.Model):
    Id= models.AutoField(primary_key=True)
    DistanciaTalu= models.CharField(max_length=15)
    DistanciaRiosCer= models.CharField(max_length=15)
    DistanciaLadeCer= models.CharField(max_length=15)
    DistanciaTorrCer= models.CharField(max_length=15)
    IdInspeccionMejo=models.ForeignKey(InspeccionMejo, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='RiesgosInsMej'
        verbose_name_plural='RiesgosInsMejs'
        db_table= 'RiesgosInsMej'

class ViasAcceInsMej(models.Model):
    Id= models.AutoField(primary_key=True)
    TipoVias= models.CharField(max_length=35)
    IdInspeccionMejo=models.ForeignKey(InspeccionMejo, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='ViasAcceInsMej'
        verbose_name_plural='ViasAcceInsMejs'
        db_table= 'ViasAcceInsMej'

class PlanMejoInsMej(models.Model):
    Id= models.AutoField(primary_key=True)
    Etapas= models.CharField(max_length=50)
    Descripcion= models.CharField(max_length=300)
    IdInspeccionMejo=models.ForeignKey(InspeccionMejo, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='PlanMejoInsMej'
        verbose_name_plural='PlanMejoInsMejs'
        db_table= 'PlanMejoInsMej'
    
class FactibilidadInsMej(models.Model):
    Id= models.AutoField(primary_key=True)
    Detalle= models.CharField(max_length=300)
    IdInspeccionMejo=models.ForeignKey(InspeccionMejo, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='FactibilidadInsMej'
        verbose_name_plural='FactibilidadInsMejs'
        db_table= 'FactibilidadInsMej'

class DescripcionMejoInsMej(models.Model):
    Id= models.AutoField(primary_key=True)
    Descripcion= models.CharField(max_length=300)
    DiasEsti= models.CharField(max_length=10)
    IdInspeccionMejo=models.ForeignKey(InspeccionMejo, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='DescripcionMejoInsMej'
        verbose_name_plural='DescripcionMejoInsMejs'
        db_table= 'DescripcionMejoInsMej'  

class EsquemasInspMej(models.Model):
    Id= models.AutoField(primary_key=True)
    EsquemaSiti= models.FileField(upload_to = "documentos/", blank=True)
    EsquemaMejo= models.FileField(upload_to = "documentos/", blank=True)
    IdInspeccionMejo=models.ForeignKey(InspeccionMejo, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='EsquemasInspMej'
        verbose_name_plural='EsquemasInspMejs'
        db_table= 'EsquemasInspMej'  

# para primera inspección
class PrimeraInspMej(models.Model):
    Id= models.AutoField(primary_key=True)
    NumeroInsp= models.CharField(max_length=25)
    Fecha= models.DateField(null=False)
    MejoraReal= models.CharField(max_length=300)
    Esquema= models.FileField(upload_to = "documentos/", blank=True)
    IdInspeccionMejo= models.ForeignKey(InspeccionMejo, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='PrimeraInspMej'
        verbose_name_plural='PrimeraInspMejs'
        db_table= 'PrimeraInspMej'

class ImagenPrimInsMej(models.Model):
    Id= models.AutoField(primary_key=True)
    Imagen = models.FileField(upload_to="documentos/", blank=True)
    IdPrimeraInspMej= models.ForeignKey(PrimeraInspMej, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='ImagenPrimInsMej'
        verbose_name_plural='ImagenPrimInsMejs'
        db_table= 'ImagenPrimInsMej'

