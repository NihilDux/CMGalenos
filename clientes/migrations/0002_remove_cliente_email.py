# Generated by Django 4.0.1 on 2023-11-22 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='email',
        ),
    ]
