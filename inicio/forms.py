from django import forms


    
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
    

class PortaMemoriasFormulario(forms.Form):
    modelo = forms.CharField(max_length=30)
<<<<<<< HEAD
    descripcion = forms.CharField(max_length=300)
=======
    descripción = forms.CharField(max_length=300)
>>>>>>> 1cbed0cd986d84e4d55170048acd85f3add4d82e
    color = forms.CharField(max_length=30)
    cantidad = forms.IntegerField()
    
class SoporteCelularesFormulario(forms.Form):
    modelo = forms.CharField(max_length=30)
<<<<<<< HEAD
    descripcion = forms.CharField(max_length=300)
=======
    descripción = forms.CharField(max_length=300)
>>>>>>> 1cbed0cd986d84e4d55170048acd85f3add4d82e
    color = forms.CharField(max_length=30)
    cantidad = forms.IntegerField()