# Generated by Django 4.0.4 on 2022-05-28 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_familia', '0002_miembros_dni_miembros_telefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='miembros',
            name='fecha_nac',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]