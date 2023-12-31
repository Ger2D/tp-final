# Generated by Django 4.2.6 on 2023-11-12 04:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inicio', '0014_remove_llaveros_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito',
            name='llaveros',
        ),
        migrations.RemoveField(
            model_name='carrito',
            name='portamemorias',
        ),
        migrations.RemoveField(
            model_name='carrito',
            name='soportecelulares',
        ),
        migrations.AddField(
            model_name='carrito',
            name='productos',
            field=models.ManyToManyField(to='inicio.llaveros'),
        ),
        migrations.AlterField(
            model_name='carrito',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
