# Generated by Django 5.1.2 on 2024-11-05 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uciapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signosvitales',
            name='temperatura',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
    ]