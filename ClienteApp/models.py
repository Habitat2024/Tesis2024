
from django.db import models
from tabnanny import verbose

from DireccionApp.models import *

# Create your models here.

class Perfil(models.Model):
    Id= models.AutoField(primary_key=True)
    Nombres= models.CharField(max_length=50)
    Apellidos= models.CharField(max_length=50)
    Dui= models.CharField(max_length=12)
    Telefono= models.CharField(max_length=10)
    Nacionalidad=models.CharField(max_length=50)
    FechaNaci=models.DateField(null=False)
    Edad= models.IntegerField()
    IdOcupacion= models.ForeignKey('ConfiguracionApp.Ocupacion', on_delete=models.CASCADE)
    Salario= models.DecimalField(max_digits=10, decimal_places=2)
    IdDistrito= models.ForeignKey('DireccionApp.Distrito',on_delete=models.CASCADE)
    Direccion= models.CharField(max_length=100)
    Correo= models.CharField(max_length=40)
    Contrasena= models.CharField(max_length=500)
    ContrasenaVeri= models.CharField(max_length=500)
    Estado= models.CharField(max_length=10)
    IdAgencia=models.ForeignKey('ConfiguracionApp.Agencia', on_delete=models.CASCADE)
    FechaRegi=models.DateField(auto_now_add=True)
    EstadoSoli= models.IntegerField()

    class Meta:
        verbose_name='Perfil'
        verbose_name_plural='Perfils'
        db_table= 'Perfil'

    def __str__(self) :
        return self.Nombres

class PerfilNoApl(models.Model):
    Id= models.AutoField(primary_key=True)
    Nombres= models.CharField(max_length=50)
    Apellidos= models.CharField(max_length=50)
    Dui= models.CharField(max_length=12)
    Telefono= models.CharField(max_length=10)
    Nacionalidad=models.CharField(max_length=50)
    Fecha=models.DateField()
    Edad= models.IntegerField()
    Salario= models.DecimalField(max_digits=10, decimal_places=2)
    Direccion= models.CharField(max_length=100)
    IdAgencia=models.ForeignKey('ConfiguracionApp.Agencia', on_delete=models.CASCADE)
    Observaciones=models.CharField(max_length=300, null=True)
    FechaRegi=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='PerfilNoApl'
        verbose_name_plural='PerfilNoApls'
        db_table= 'PerfilNoApl'
    




    
    
    