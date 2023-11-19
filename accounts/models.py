from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class DatosExtra(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   biografia = models.CharField(max_length=300)
   avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
   telefono = models.CharField(max_length=15, null=True)
   
