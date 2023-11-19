from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextFormField

    



class BaseProductoForm(forms.Form):
    modelo = forms.CharField(max_length=30)
    descripcion = RichTextFormField()
    color = forms.CharField(max_length=30)
    cantidad = forms.IntegerField()
    fecha = forms.DateTimeField(initial=timezone.now)
    # usuario = forms.CharField(max_length=30)

class LlaveroFormulario(BaseProductoForm):
    
    pass

class ActualizarLlaveroFormulario(BaseProductoForm):
   
    pass

class PortaMemoriasFormulario(BaseProductoForm):
    
    pass

class ActualizarPortaMemoriasFormulario(BaseProductoForm):
    
    pass

class SoporteCelularesFormulario(BaseProductoForm):
    
    pass

class ActualizarSoporteCelularesFormulario(BaseProductoForm):
    
    pass