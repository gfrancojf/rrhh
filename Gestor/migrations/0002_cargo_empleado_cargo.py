# Generated by Django 4.0.6 on 2022-07-20 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gestor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_at', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('update_at', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('delete_at', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('cargo', models.CharField(max_length=60, unique=True, verbose_name='Cargo')),
                ('imgref', models.ImageField(blank=True, null=True, upload_to='empresa/cargo', verbose_name='Imagen de Referencia')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.AddField(
            model_name='empleado',
            name='cargo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Gestor.cargo'),
            preserve_default=False,
        ),
    ]