# Generated by Django 4.2.6 on 2023-11-12 01:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inicio', '0009_rename_descripcion_llaveros_descripción_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='llaveros',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
