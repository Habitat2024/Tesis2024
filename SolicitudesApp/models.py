from django.db import models
from ConfiguracionApp.models import *
from ClienteApp.models import Perfil

# Create your models here.
class Solicitud(models.Model):
    Id= models.AutoField(primary_key=True)
    TipoObra=models.CharField(max_length=10)
    Fecha=models.DateField(null=False)
    Numero=models.CharField(max_length=12)
    Comunidad=models.CharField(max_length=80)
    Area=models.CharField(max_length=15)
    Tipo=models.CharField(max_length=10) # si la solicitud es micro o natural
    TipoIngr=models.CharField(max_length=10,null=True)# solo para natural, tipo empleo o remesa
    Estado=models.CharField(max_length=15)
    Observaciones=models.CharField(max_length=300, null=True)
    EstadoSoli=models.IntegerField(null=True)
    IdPerfil=models.ForeignKey(Perfil, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Solicitud'
        verbose_name_plural='Solicitudes'
        db_table= 'Solicitud'

class DatosPers(models.Model): # para cliente
      Id= models.AutoField(primary_key=True)      
      LugarDuiCli=models.CharField(max_length=100)
      FechaDuiCli=models.DateField()
      LugarNaciCli=models.CharField(max_length=100)
      EstadoCiviCli=models.CharField(max_length=30)
      GeneroClie=models.CharField(max_length=12)
      Profesion=models.CharField(max_length=40)
      EstadoClie= models.CharField(max_length=10)
      IdSolicitud=models.ForeignKey(Solicitud, on_delete=models.CASCADE)
      EstadoSoli=models.IntegerField(null=True)

      class Meta:
            verbose_name='DatosPers'
            verbose_name_plural='DatosPerss'
            db_table= 'DatosPers'

class DatosPersFia(models.Model): # para tipo conyuge o codeudor
       Id= models.AutoField(primary_key=True)
       Tipo=models.CharField(max_length=12)
       NombreFiad= models.CharField(max_length=50)
       ApellidoFiad= models.CharField(max_length=50)
       DuiFiad= models.CharField(max_length=12)
       LugarDuiFia= models.CharField(max_length=30)
       FechaDuiFia=models.DateField(null=False)
       FechaNaciFia=models.DateField(null=False)
       LugarNaciFia= models.CharField(max_length=30)
       EdadFiad= models.IntegerField()      
       EstadoCiviFiad=models.CharField(max_length=30)
       GeneroFiad=models.CharField(max_length=12)
       ProfecionFiad=models.CharField(max_length=30)
       EstadoFiad= models.IntegerField()
       IdSolicitud=models.ForeignKey(Solicitud, on_delete=models.CASCADE)
       EstadoSoli=models.IntegerField(null=True)

       class Meta:
            verbose_name='DatosPersFia'
            verbose_name_plural='DatosPersFias'
            db_table= 'DatosPersFia'

class GrupoFami(models.Model):
    Id= models.AutoField(primary_key=True)
    IdSolicitud=models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    Nombre= models.CharField(max_length=50)
    Edad= models.CharField(max_length=10)
    Salario= models.DecimalField(max_digits=10, decimal_places=2)
    Trabajo=models.CharField(max_length=50)
    Parentesco=models.CharField(max_length=50)
    EstadoSoli=models.IntegerField(null=True)

    class Meta:
        verbose_name='GrupoFami'
        verbose_name_plural='GrupoFami'
        db_table= 'GrupoFami'

class Domicilio(models.Model):
    Id= models.AutoField(primary_key=True)
    IdSolicitud=models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    Direccion=models.CharField(max_length=100)
    Referencia=models.CharField(max_length=50) 
    Telefono=models.CharField(max_length=15)
    ResideDesd=models.CharField(max_length=50)
    CondicionVivi=models.CharField(max_length=50)
    LugarTrab=models.CharField(max_length=100)
    ActividadMicr=models.CharField(max_length=50, null=True)# para micro
    JefeInme=models.CharField(max_length=50, null=True)#para natural
    TiempoEmprTieFun=models.CharField(max_length=50)
    SalarioIngr=models.DecimalField(max_digits=10, decimal_places=2)
    DireccionTrabMic=models.CharField(max_length=100)
    TelefonoTrabMic=models.CharField(max_length=15)
    Tipo= models.CharField(max_length=15)
    EstadoSoli=models.IntegerField(null=True)

    class Meta:
        verbose_name='Domicilio'
        verbose_name_plural='Domicilios'
        db_table= 'Domicilio'

class DatosObra(models.Model):
    Id= models.AutoField(primary_key=True)
    IdSolicitud=models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    IdAlternativa=models.ForeignKey('ConfiguracionApp.Alternativa', on_delete=models.CASCADE)
    Dueno=models.CharField(max_length=50)
    Parentesco=models.CharField(max_length=50)
    DireccionExac=models.CharField(max_length=100)
    IdModeloVivi=models.ForeignKey('ConfiguracionApp.ModeloVivi', on_delete=models.CASCADE)
    DetalleAdic=models.CharField(max_length=80, null=True)
    Presupuesto=models.DecimalField(max_digits=15, decimal_places=2)
    EstadoSoli=models.IntegerField(null=True)

    class Meta:
        verbose_name='DatosObra'
        verbose_name_plural='DatosObras'
        db_table= 'DatosObra'

class Detalle(models.Model):
    Id= models.AutoField(primary_key=True)
    IdSolicitud=models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    Monto=models.DecimalField(max_digits=10, decimal_places=2)
    Plazo=models.CharField(max_length=50)
    Cuota=models.DecimalField(max_digits=10, decimal_places=2)
    FormaPago=models.CharField(max_length=15)
    FechaPago=models.CharField(max_length=30)
    EstadoSoli=models.IntegerField(null=True)

    class Meta:
        verbose_name='Detalle'
        verbose_name_plural='Detalles'
        db_table= 'Detalle'

class ExperienciaCred(models.Model):
    Id= models.AutoField(primary_key=True)
    IdSolicitud=models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    Lugar=models.CharField(max_length=30,null=True)
    Monto=models.DecimalField(max_digits=10, decimal_places=2, null=True)
    FechaOtor=models.DateField(null=True)
    Estado=models.CharField(max_length=12,null=True)
    Cuota=models.DecimalField(max_digits=10, decimal_places=2, null=True)
    PoseeExpe=models.BooleanField()
    EstadoSoli=models.IntegerField(null=True)

    class Meta:
        verbose_name='ExperienciaCred'
        verbose_name_plural='ExperienciaCreds'
        db_table= 'ExperienciaCred'

class Referencias(models.Model):
    Id= models.AutoField(primary_key=True)
    IdSolicitud=models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    Nombre=models.CharField(max_length=50)
    Parentesco=models.CharField(max_length=15)
    Domicilio=models.CharField(max_length=100)
    Telefono=models.CharField(max_length=12)
    EstadoSoli=models.IntegerField(null=True)

    class Meta:
        verbose_name='Referencias'
        verbose_name_plural='Referencias'
        db_table= 'Referencias'

class Comentarios(models.Model):
    Id= models.AutoField(primary_key=True)
    IdSolicitud=models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    ComentarioNeceVivMej=models.CharField(max_length=200)
    ComentarioEvalEst=models.CharField(max_length=200)
    ComentarioGaraOfr=models.CharField(max_length=200)
    EstadoSoli=models.IntegerField(null=True)

    class Meta:
        verbose_name='Comentarios'
        verbose_name_plural='Comentarios'
        db_table= 'Comentarios'

class Medio(models.Model):
    Id= models.AutoField(primary_key=True)
    IdSolicitud=models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    RedesSoci=models.CharField(max_length=25)
    Pvv=models.CharField(max_length=25)
    Referenciado=models.CharField(max_length=25)
    Perifoneo=models.CharField(max_length=25)
    Radio=models.CharField(max_length=25)
    FeriaVivi=models.CharField(max_length=25)
    CampanaProm=models.CharField(max_length=25)
    Otros=models.CharField(max_length=25)
    Especifique=models.CharField(max_length=80)
    EstadoSoli=models.IntegerField(null=True)
    
    class Meta:
        verbose_name='Medio'
        verbose_name_plural='Medios'
        db_table= 'Medio'

