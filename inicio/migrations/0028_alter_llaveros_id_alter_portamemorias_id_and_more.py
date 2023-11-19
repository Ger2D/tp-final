# Generated by Django 4.2.6 on 2023-11-18 17:29

from django.db import migrations, models
import inicio.models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0027_idcounter_alter_llaveros_id_alter_portamemorias_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='llaveros',
            name='id',
            field=models.IntegerField(default=inicio.models.IDCounter.get_next_id, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='portamemorias',
            name='id',
            field=models.IntegerField(default=inicio.models.IDCounter.get_next_id, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='soportecelulares',
            name='id',
            field=models.IntegerField(default=inicio.models.IDCounter.get_next_id, primary_key=True, serialize=False),
        ),
    ]
