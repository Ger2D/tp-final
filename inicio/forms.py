from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextFormField

    
<<<<<<< HEAD
=======
class PedidoFormulario(forms.Form):
    modelo = forms.CharField(max_length=30)
<<<<<<< HEAD
    descripcion = forms.CharField(max_length=300)
=======
    descripción = forms.CharField(max_length=300)
>>>>>>> 1cbed0cd986d84e4d55170048acd85f3add4d82e
    color = forms.CharField(max_length=30)
    cantidad = forms.IntegerField()
    
class LlaveroFormulario(forms.Form):
    modelo = forms.CharField(max_length=30)
<<<<<<< HEAD
    descripcion = forms.CharField(max_length=300)
=======
    descripción = forms.CharField(max_length=300)
>>>>>>> 1cbed0cd986d84e4d55170048acd85f3add4d82e
    color = forms.CharField(max_length=30)
    cantidad = forms.IntegerField()
    
>>>>>>> eb6945b16b3580dbd5ca90e60ee5bd82b261f89e



class BaseProductoForm(forms.Form):
    modelo = forms.CharField(max_length=30)
<<<<<<< HEAD
    descripcion = RichTextFormField()
=======
<<<<<<< HEAD
    descripcion = forms.CharField(max_length=300)
=======
    descripción = forms.CharField(max_length=300)
>>>>>>> 1cbed0cd986d84e4d55170048acd85f3add4d82e
>>>>>>> eb6945b16b3580dbd5ca90e60ee5bd82b261f89e
    color = forms.CharField(max_length=30)
    cantidad = forms.IntegerField()
    fecha = forms.DateTimeField(initial=timezone.now)
    # usuario = forms.CharField(max_length=30)

class LlaveroFormulario(BaseProductoForm):
    
<<<<<<< HEAD
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
=======
class SoporteCelularesFormulario(forms.Form):
    modelo = forms.CharField(max_length=30)
<<<<<<< HEAD
    descripcion = forms.CharField(max_length=300)
=======
    descripción = forms.CharField(max_length=300)
>>>>>>> 1cbed0cd986d84e4d55170048acd85f3add4d82e
    color = forms.CharField(max_length=30)
    cantidad = forms.IntegerField()
>>>>>>> eb6945b16b3580dbd5ca90e60ee5bd82b261f89e
