# Generated by Django 4.2.6 on 2023-11-12 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0016_llaveros_usuario_delete_carrito'),
    ]

    operations = [
        migrations.RenameField(
            model_name='llaveros',
            old_name='usuario',
            new_name='sorete',
        ),
    ]
