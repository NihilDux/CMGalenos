# Generated by Django 4.0.1 on 2023-11-21 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Centro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='nombre')),
            ],
        ),
    ]