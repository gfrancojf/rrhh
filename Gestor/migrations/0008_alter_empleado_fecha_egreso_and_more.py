# Generated by Django 4.0.6 on 2022-07-20 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestor', '0007_alter_empleado_nac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='fecha_egreso',
            field=models.DateField(blank=True, null=True, verbose_name='F. de Egreso'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='observacion',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Observaciones'),
        ),
    ]