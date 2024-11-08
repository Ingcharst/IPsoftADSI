# Generated by Django 5.1.1 on 2024-11-08 03:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacion', models.IntegerField(blank=True, null=True)),
                ('historia', models.IntegerField(blank=True, null=True)),
                ('fecha_hora', models.DateTimeField(auto_now_add=True, null=True)),
                ('nota_enfermeria', models.CharField(blank=True, max_length=500, null=True)),
                ('usuario', models.CharField(max_length=500, null=True)),
                ('medicamento', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Observacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(blank=True, max_length=500, null=True)),
                ('fecha_horas', models.DateTimeField(auto_now_add=True, null=True)),
                ('nota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='observaciones', to='notas_enfermeria.nota')),
            ],
        ),
    ]
