# Generated by Django 4.2.6 on 2023-11-01 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0008_delete_pedido'),
    ]

    operations = [
        migrations.RenameField(
            model_name='llaveros',
            old_name='descripcion',
            new_name='descripción',
        ),
        migrations.RenameField(
            model_name='portamemorias',
            old_name='descripcion',
            new_name='descripción',
        ),
        migrations.RenameField(
            model_name='soportecelulares',
            old_name='descripcion',
            new_name='descripción',
        ),
    ]
