# Generated by Django 4.2.6 on 2023-10-31 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0005_rename_llavero_pedido'),
    ]

    operations = [
        migrations.CreateModel(
            name='Llaveros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('color', models.CharField(max_length=30)),
                ('cantidad', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PortaMemorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('color', models.CharField(max_length=30)),
                ('cantidad', models.IntegerField(null=True)),
            ],
        ),
    ]
