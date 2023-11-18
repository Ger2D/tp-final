from django.db import models

    
    
   
    
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
