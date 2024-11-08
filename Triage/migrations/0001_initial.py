# Generated by Django 5.1.1 on 2024-11-08 03:57

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NivelTriage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('color', models.CharField(choices=[('R', 'Rojo'), ('N', 'Naranja'), ('A', 'Amarillo'), ('V', 'Verde'), ('Az', 'Azul')], max_length=50)),
                ('tiempo_maximo_atencion', models.IntegerField(help_text='Tiempo máximo de atención en minutos')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('documento_identidad', models.CharField(max_length=20, unique=True)),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SignosVitales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateTimeField(auto_now_add=True)),
                ('presion_arterial_sistolica', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(300)])),
                ('presion_arterial_diastolica', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(200)])),
                ('frecuencia_cardiaca', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(300)])),
                ('frecuencia_respiratoria', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('temperatura', models.DecimalField(decimal_places=1, max_digits=4)),
                ('saturacion_oxigeno', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='signos_vitales', to='Triage.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Triage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateTimeField(auto_now_add=True)),
                ('motivo_consulta', models.TextField()),
                ('observaciones', models.TextField(blank=True)),
                ('nivel_triage', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Triage.niveltriage')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='triages', to='Triage.paciente')),
                ('signos_vitales', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Triage.signosvitales')),
            ],
        ),
    ]
