# Generated by Django 4.2.6 on 2023-11-01 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0006_llaveros_portamemorias'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoporteCelulares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('color', models.CharField(max_length=30)),
                ('cantidad', models.IntegerField(null=True)),
            ],
        ),
    ]
