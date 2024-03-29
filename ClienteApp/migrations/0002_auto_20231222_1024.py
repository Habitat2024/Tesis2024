# Generated by Django 3.0.6 on 2023-12-22 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ConfiguracionApp', '0001_initial'),
        ('DireccionApp', '0001_initial'),
        ('ClienteApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilnoapl',
            name='IdAgencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConfiguracionApp.Agencia'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='IdAgencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConfiguracionApp.Agencia'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='IdDistrito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DireccionApp.Distrito'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='IdOcupacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConfiguracionApp.Ocupacion'),
        ),
    ]
