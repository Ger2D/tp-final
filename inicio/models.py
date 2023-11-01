from django.db import models

    
    
   
    
class Llaveros(models.Model):
    modelo = models.CharField(max_length=30)
    descripción = models.TextField()
    color = models.CharField(max_length=30)
    cantidad = models.IntegerField(null=True)
    
    def __str__(self):
        return f'{self.id} - {self.modelo} - {self.descripción} - {self.color} - {self.cantidad}'
    
    
class PortaMemorias(models.Model):
    modelo = models.CharField(max_length=30)
    descripción = models.TextField()
    color = models.CharField(max_length=30)
    cantidad = models.IntegerField(null=True)
    
    def __str__(self):
        return f'{self.id} - {self.modelo} - {self.descripción} - {self.color} - {self.cantidad}'
    
class SoporteCelulares(models.Model):
    modelo = models.CharField(max_length=30)
    descripción = models.TextField()
    color = models.CharField(max_length=30)
    cantidad = models.IntegerField(null=True)
    
    def __str__(self):
        return f'{self.id} - {self.modelo} - {self.descripción} - {self.color} - {self.cantidad}'
    
    
