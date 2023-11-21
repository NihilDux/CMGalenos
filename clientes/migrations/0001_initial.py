# Generated by Django 4.0.1 on 2023-11-21 14:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medicos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=9)),
                ('telefono', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="El número debe estar en el siguiente formato,  '+56912345678'.", regex='^\\+?56?9?\\d{8}$')], verbose_name='Telefono')),
                ('run', models.CharField(max_length=50, unique=True, verbose_name='run')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agenda', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='consulta', to='medicos.agenda')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consulta', to='clientes.cliente')),
            ],
            options={
                'unique_together': {('agenda', 'cliente')},
            },
        ),
    ]