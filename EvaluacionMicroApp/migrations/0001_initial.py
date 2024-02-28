# Generated by Django 3.0.6 on 2023-12-22 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ClienteApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceSituMic',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('TipoNego', models.CharField(max_length=100)),
                ('Estado', models.IntegerField()),
                ('IdPerfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ClienteApp.Perfil')),
            ],
            options={
                'verbose_name': 'BalanceSituMic',
                'verbose_name_plural': 'BalanceSituMics',
                'db_table': 'BalanceSituMic',
            },
        ),
        migrations.CreateModel(
            name='EgresoFlujMic',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Alimentacion', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Educacion', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Transporte', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Salud', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Afp', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Servicios', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Alquiler', models.DecimalField(decimal_places=2, max_digits=15)),
                ('PorcentajePlan', models.DecimalField(decimal_places=2, max_digits=15)),
                ('PorcentajeVent', models.DecimalField(decimal_places=2, max_digits=15)),
                ('PorcentajeHplhes', models.DecimalField(decimal_places=2, max_digits=15)),
                ('OtrosDesc', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Recreacion', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Imprevistos', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Total', models.DecimalField(decimal_places=2, max_digits=15)),
                ('IdBalanceSituMic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EvaluacionMicroApp.BalanceSituMic')),
            ],
            options={
                'verbose_name': 'EgresoFlujMic',
                'verbose_name_plural': 'EgresoFlujMics',
                'db_table': 'EgresoFlujMic',
            },
        ),
        migrations.CreateModel(
            name='PasivoBalaSit',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('TotalCircPas', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Proveedores', models.DecimalField(decimal_places=2, max_digits=15)),
                ('CuentasPorPag', models.DecimalField(decimal_places=2, max_digits=15)),
                ('PrestamosCortPla', models.DecimalField(decimal_places=2, max_digits=15)),
                ('FijoPasi', models.DecimalField(decimal_places=2, max_digits=15)),
                ('PrestamosLargPla', models.DecimalField(decimal_places=2, max_digits=15)),
                ('TotalPasi', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Patrimonio', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Capital', models.DecimalField(decimal_places=2, max_digits=15)),
                ('PasivoMasPat', models.DecimalField(decimal_places=2, max_digits=15)),
                ('IdBalanceSituMic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EvaluacionMicroApp.BalanceSituMic')),
            ],
            options={
                'verbose_name': 'PasivoBalaSit',
                'verbose_name_plural': 'PasivoBalaSits',
                'db_table': 'PasivoBalaSit',
            },
        ),
        migrations.CreateModel(
            name='IngresoFlujMic',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Negocio', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Remesas', models.DecimalField(decimal_places=2, max_digits=15)),
                ('TotalIngrMic', models.DecimalField(decimal_places=2, max_digits=15)),
                ('IdEgresoFlujMic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EvaluacionMicroApp.EgresoFlujMic')),
            ],
            options={
                'verbose_name': 'IngresoFlujMic',
                'verbose_name_plural': 'IngresoFlujMics',
                'db_table': 'IngresoFlujMic',
            },
        ),
        migrations.CreateModel(
            name='EstadoResuMic',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('VentasTota', models.DecimalField(decimal_places=2, max_digits=15)),
                ('CostoVent', models.DecimalField(decimal_places=2, max_digits=15)),
                ('UtilidadBrut', models.DecimalField(decimal_places=2, max_digits=15)),
                ('GastosGral', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Transporte', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Servicios', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Impuestos', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Alquiler', models.DecimalField(decimal_places=2, max_digits=15)),
                ('CuotaPres', models.DecimalField(decimal_places=2, max_digits=15)),
                ('ImprevistosEstaRes', models.DecimalField(decimal_places=2, max_digits=15)),
                ('UtilidadNeta', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Mensual', models.DecimalField(decimal_places=2, max_digits=15)),
                ('IdBalanceSituMic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EvaluacionMicroApp.BalanceSituMic')),
            ],
            options={
                'verbose_name': 'EstadoResuMic',
                'verbose_name_plural': 'EstadoResuMics',
                'db_table': 'EstadoResuMic',
            },
        ),
        migrations.CreateModel(
            name='CapacidadPagoMic',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('PorcentajeEnde', models.CharField(max_length=10)),
                ('Disponible', models.DecimalField(decimal_places=2, max_digits=15)),
                ('PorcentajeDisp', models.CharField(max_length=10)),
                ('Cuota', models.DecimalField(decimal_places=2, max_digits=15)),
                ('PorcentajeCuot', models.CharField(max_length=10)),
                ('Superavit', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Deficit', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Estado', models.CharField(max_length=10)),
                ('IdEgresoFlujMic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EvaluacionMicroApp.EgresoFlujMic')),
            ],
            options={
                'verbose_name': 'CapacidadPagoMic',
                'verbose_name_plural': 'CapacidadPagoMics',
                'db_table': 'CapacidadPagoMic',
            },
        ),
        migrations.CreateModel(
            name='ActivoBalaSit',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('TotalCircAct', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Caja', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Bancos', models.DecimalField(decimal_places=2, max_digits=15)),
                ('CuentasPorCob', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Inventarios', models.DecimalField(decimal_places=2, max_digits=15)),
                ('TotalFijoAct', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Mobiliario', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Terrenos', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Vehiculos', models.DecimalField(decimal_places=2, max_digits=15)),
                ('TotalActi', models.DecimalField(decimal_places=2, max_digits=15)),
                ('IdBalanceSituMic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EvaluacionMicroApp.BalanceSituMic')),
            ],
            options={
                'verbose_name': 'ActivoBalaSit',
                'verbose_name_plural': 'ActivoBalaSits',
                'db_table': 'ActivoBalaSit',
            },
        ),
    ]
