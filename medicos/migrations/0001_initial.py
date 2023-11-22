# Generated by Django 4.0.1 on 2023-11-21 21:23

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import medicos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Centro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='nombre')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('run', models.CharField(max_length=200, verbose_name='RUN')),
                ('telefono', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="El número debe estar en el siguiente formato,  '+56912345678'.", regex='^\\+?56?9?\\d{8}$')], verbose_name='telefono')),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicos', to='medicos.especialidad')),
            ],
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField(help_text='Introduzca una fecha para el calendario', validators=[medicos.models.validar_dia])),
                ('horario', models.CharField(choices=[('1', '07:00 a 08:00'), ('2', '08:00 a 09:00'), ('3', '09:00 a 10:00'), ('4', '10:00 a 11:00'), ('5', '11:00 a 12:00'), ('6', '13:00 a 14:00'), ('7', '16:00 a 17:00')], max_length=10)),
                ('centro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agenda', to='medicos.centro')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agenda', to='medicos.medico')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'unique_together': {('horario', 'dia')},
            },
        ),
    ]
