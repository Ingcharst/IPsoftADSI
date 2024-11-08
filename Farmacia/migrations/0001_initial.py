# Generated by Django 5.1.1 on 2024-11-07 03:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('historia_clinica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_Cat', models.CharField(max_length=10)),
                ('categoria', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Insumos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('referencia', models.CharField(max_length=10)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_lab', models.CharField(max_length=10)),
                ('laboratorio', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Presentacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_presentacion', models.CharField(max_length=5)),
                ('presentacion', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.CharField(max_length=20)),
                ('proveedor', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=50)),
                ('celular', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_mov',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_tipo', models.SmallIntegerField()),
                ('tipo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_und', models.CharField(max_length=5)),
                ('nombre_und', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('referencia', models.CharField(max_length=10)),
                ('descripcion', models.TextField()),
                ('componente', models.CharField(max_length=100)),
                ('concentracion', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField()),
                ('lote', models.CharField(max_length=10)),
                ('vencimiento', models.DateTimeField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Farmacia.categoria')),
                ('laboratorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Farmacia.laboratorio')),
            ],
            options={
                'permissions': [('can_access_farmacia', 'Can access farmacia module')],
            },
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_factura', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='historia_clinica.paciente')),
                ('medicamentos', models.ManyToManyField(to='Farmacia.medicamento')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Farmacia.proveedores')),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('cantidad', models.CharField(max_length=50)),
                ('tratamiento', models.TextField()),
                ('estado', models.CharField(default='Falta de medicamento', max_length=50)),
                ('cantidad_entregada', models.CharField(default=0, max_length=50)),
                ('fecha_entrega', models.DateTimeField(blank=True, null=True)),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Farmacia.medicamento')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='historia_clinica.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Movimientos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_factura', models.IntegerField()),
                ('usuario', models.IntegerField()),
                ('tercero', models.IntegerField()),
                ('referencia', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('fecha', models.DateField()),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Farmacia.tipo_mov')),
            ],
        ),
    ]