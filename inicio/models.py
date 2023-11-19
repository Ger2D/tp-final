
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField




class IDCounter(models.Model):
    next_id = models.IntegerField(default=1)

    @classmethod
    def get_next_id(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        current_id = obj.next_id
        obj.next_id += 1
        obj.save()
        return current_id

class ProductoBase(models.Model):
    id = models.IntegerField(primary_key=True, default=IDCounter.get_next_id)
    modelo = models.CharField(max_length=30)
    descripcion = RichTextField(default='no hay descripción')
    color = models.CharField(max_length=30)
    cantidad = models.IntegerField(null=True)
    fecha = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        abstract = True   

    def __str__(self):
        return f'Modelo: {self.modelo} - Color: {self.color} - Cantidad: {self.cantidad}'

class Llaveros(ProductoBase):
    pass

class PortaMemorias(ProductoBase):
    pass

class SoporteCelulares(ProductoBase):
    pass






