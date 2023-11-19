
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







# from django.db import models
# from django.contrib.auth.models import User
# from django import forms
# from django.utils import timezone
# from ckeditor.fields import RichTextField




    
<<<<<<< HEAD
# class Llaveros(models.Model):
#     id = models.AutoField(primary_key=True)
#     modelo = models.CharField(max_length=30 )
#     descripcion = RichTextField(null=True)
#     color = models.CharField(max_length=30)
#     cantidad = models.IntegerField(null=True)
#     fecha = models.DateTimeField(default=timezone.now)
#     usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    
#     def __str__(self):
#         return f'{self.modelo} - {self.color} - {self.cantidad}'

    
# class PortaMemorias(models.Model):
#     id = models.AutoField(primary_key=True)
#     modelo = models.CharField(max_length=30)
#     descripcion = RichTextField(null=True)
#     color = models.CharField(max_length=30)
#     cantidad = models.IntegerField(null=True)
#     fecha = models.DateTimeField(default=timezone.now)
#     usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    
#     def __str__(self):
#         return f'{self.modelo} - {self.color} - {self.cantidad}'
    
# class SoporteCelulares(models.Model):
#     id = models.AutoField(primary_key=True)
#     modelo = models.CharField(max_length=30)
#     descripcion = RichTextField(null=True)
#     color = models.CharField(max_length=30)
#     cantidad = models.IntegerField(null=True)
#     fecha = models.DateTimeField(default=timezone.now)
#     usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    
#     def __str__(self):
#         return f'{self.modelo} - {self.color} - {self.cantidad}'

=======
    
   
    
class Llaveros(models.Model):
    modelo = models.CharField(max_length=30)
<<<<<<< HEAD
    descripcion = models.TextField()
=======
    descripción = models.TextField()
>>>>>>> 1cbed0cd986d84e4d55170048acd85f3add4d82e
    color = models.CharField(max_length=30)
    cantidad = models.IntegerField(null=True)
    
    def __str__(self):
<<<<<<< HEAD
        return f'{self.id} - {self.modelo} - {self.descripcion} - {self.color} - {self.cantidad}'
=======
        return f'{self.id} - {self.modelo} - {self.descripción} - {self.color} - {self.cantidad}'
>>>>>>> 1cbed0cd986d84e4d55170048acd85f3add4d82e
    
    
class PortaMemorias(models.Model):
    modelo = models.CharField(max_length=30)
<<<<<<< HEAD
    descripcion = models.TextField()
=======
    descripción = models.TextField()
>>>>>>> 1cbed0cd986d84e4d55170048acd85f3add4d82e
    color = models.CharField(max_length=30)
    cantidad = models.IntegerField(null=True)
    
    def __str__(self):
<<<<<<< HEAD
        return f'{self.id} - {self.modelo} - {self.descripcion} - {self.color} - {self.cantidad}'
    
class SoporteCelulares(models.Model):
    modelo = models.CharField(max_length=30)
    descripcion = models.TextField()
=======
        return f'{self.id} - {self.modelo} - {self.descripción} - {self.color} - {self.cantidad}'
    
class SoporteCelulares(models.Model):
    modelo = models.CharField(max_length=30)
    descripción = models.TextField()
>>>>>>> 1cbed0cd986d84e4d55170048acd85f3add4d82e
    color = models.CharField(max_length=30)
    cantidad = models.IntegerField(null=True)
    
    def __str__(self):
<<<<<<< HEAD
        return f'{self.id} - {self.modelo} - {self.descripcion} - {self.color} - {self.cantidad}'
    
    
# class Pedido(models.Model):
#     modelo = models.CharField(max_length=30)
#     descripcion = models.TextField()
#     color = models.CharField(max_length=30)
#     cantidad = models.IntegerField(null=True)
    
#     def __str__(self):
#         return f'{self.id} - {self.modelo} - {self.descripcion} - {self.color} - {self.cantidad}'
=======
        return f'{self.id} - {self.modelo} - {self.descripción} - {self.color} - {self.cantidad}'
    
    
>>>>>>> 1cbed0cd986d84e4d55170048acd85f3add4d82e
>>>>>>> eb6945b16b3580dbd5ca90e60ee5bd82b261f89e
