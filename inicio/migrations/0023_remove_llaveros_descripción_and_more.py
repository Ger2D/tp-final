# Generated by Django 4.2.6 on 2023-11-18 16:31

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0022_portamemorias_fecha_soportecelulares_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='llaveros',
            name='descripción',
        ),
        migrations.RemoveField(
            model_name='portamemorias',
            name='descripción',
        ),
        migrations.RemoveField(
            model_name='soportecelulares',
            name='descripción',
        ),
        migrations.AddField(
            model_name='llaveros',
            name='descripcion',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='portamemorias',
            name='descripcion',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='soportecelulares',
            name='descripcion',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='llaveros',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='portamemorias',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='soportecelulares',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
