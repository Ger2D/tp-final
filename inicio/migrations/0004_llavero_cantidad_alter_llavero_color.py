# Generated by Django 4.2.6 on 2023-10-29 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_rename_paleta_llavero_rename_anio_llavero_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='llavero',
            name='cantidad',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='llavero',
            name='color',
            field=models.CharField(max_length=30),
        ),
    ]
