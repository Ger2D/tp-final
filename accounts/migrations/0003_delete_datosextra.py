# Generated by Django 4.2.6 on 2023-11-14 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_datosextradeusuasio_datosextra'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DatosExtra',
        ),
    ]