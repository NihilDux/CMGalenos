# Generated by Django 4.0.1 on 2023-11-23 15:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='run',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message="El número debe estar en el algunos de los siguientes formatos: '1.111.111-1' o '11.111.111-1'.", regex='^\\d{1,2}\\d.\\d{3}\\d.\\d{3}-\\d{1}$')], verbose_name='run'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='telefono',
            field=models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="El número debe estar en el siguiente formato,  '+56912345678'.", regex='^\\+569\\d{8}$')], verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='run',
            field=models.CharField(blank=True, max_length=12, null=True, validators=[django.core.validators.RegexValidator(message="El número debe estar en el algunos de los siguientes formatos: '1.111.111-1' o '11.111.111-1'.", regex='^\\d{1,2}\\d.\\d{3}\\d.\\d{3}-\\d{1}$')], verbose_name='run'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='telefono',
            field=models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="El número debe estar en el siguiente formato,  '+56912345678'.", regex='^\\+569\\d{8}$')], verbose_name='telefono'),
        ),
    ]