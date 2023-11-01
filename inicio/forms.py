from django import forms


    
class PedidoFormulario(forms.Form):
    modelo = forms.CharField(max_length=30)
    descripción = forms.CharField(max_length=300)
    color = forms.CharField(max_length=30)
    cantidad = forms.IntegerField()
    
class LlaveroFormulario(forms.Form):
    modelo = forms.CharField(max_length=30)
    descripción = forms.CharField(max_length=300)
    color = forms.CharField(max_length=30)
    cantidad = forms.IntegerField()
    

class PortaMemoriasFormulario(forms.Form):
    modelo = forms.CharField(max_length=30)
    descripción = forms.CharField(max_length=300)
    color = forms.CharField(max_length=30)
    cantidad = forms.IntegerField()
    
class SoporteCelularesFormulario(forms.Form):
    modelo = forms.CharField(max_length=30)
    descripción = forms.CharField(max_length=300)
    color = forms.CharField(max_length=30)
    cantidad = forms.IntegerField()