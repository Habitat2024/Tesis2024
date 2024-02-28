from django.db import models
from SolicitudesApp.models import *
from ConfiguracionApp.models import *

# Create your models here.
class SolicitudInscSeg(models.Model):
    Id= models.AutoField(primary_key=True)
    MontosAsegAnt= models.DecimalField(decimal_places=2, max_digits=15)
    NuevoMontAse= models.DecimalField(decimal_places=2, max_digits=15)
    MontoTotaAse= models.DecimalField(decimal_places=2, max_digits=15)
    Plazo= models.CharField(max_length=10)
    Garantia=models.CharField(max_length=50)
    Estatura= models.CharField(max_length=15)
    Peso= models.CharField(max_length=15)
    DesignoBene= models.CharField(max_length=30)
    IdSolicitud= models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='SolicitudInscSeg'
        verbose_name_plural='SolicitudInscSegs'
        db_table= 'SolicitudInscSeg'

class SolicitudInscSegPad(models.Model):
    Id= models.AutoField(primary_key=True)
    IdSolicitudInscSegEnf= models.ForeignKey(SolicitudInscSegEnf, on_delete=models.CASCADE)
    IdPerfil= models.ForeignKey(Perfil, on_delete=models.CASCADE)
    FechaPade=models.DateField(null=True, blank=True)
    TratamientoReci=models.CharField(max_length=200)
    SituacionActu=models.CharField(max_length=100)
    Estado= models.CharField(max_length=10)
      
    class Meta:
        verbose_name='SolicitudInscSegPad'
        verbose_name_plural='SolicitudInscSegPads'
        db_table= 'SolicitudInscSegPad'

class SolicitudInscSegDefAmpDefFis(models.Model):
    Id= models.AutoField(primary_key=True)
    TieneDefoAmpDefFis=models.CharField(max_length=5)
    DetallesDefoAmpDefFis=models.CharField(max_length=50)
    FumaCigaPip=models.CharField(max_length=5)
    CuantosDia=models.CharField(max_length=15)
    BebidasAlco=models.CharField(max_length=5)
    FrecuenciaBebiAlc=models.CharField(max_length=25)
    TratamientoMedi=models.CharField(max_length=5)
    DetalleTratMed=models.CharField(max_length=50)
    PracticaActiDep=models.CharField(max_length=5)
    ClaseActiDep=models.CharField(max_length=25)
    FrecuenciaActiDep=models.CharField(max_length=25)
    SeguroDese=models.CharField(max_length=5)
    IdSolicitudInscSeg= models.ForeignKey(SolicitudInscSeg, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='SolicitudInscSegDefAmpDefFis'
        verbose_name_plural='SolicitudInscSegDefAmpDefFiss'
        db_table= 'SolicitudInscSegDefAmpDefFis'

