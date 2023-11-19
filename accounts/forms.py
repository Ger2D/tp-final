from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class MiFormularioDeCreacion(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(label='Usuario')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {'username': '', 'email': '','password1': '','password2': ''}
        

class MiFormularioDeEdicionDePerfil(UserChangeForm):
    password = None
    email = forms.EmailField(label='Cambiar email', required = False)
    first_name = forms.CharField(label='Cambiar nombre', required = False)
    last_name = forms.CharField(label='Cambiar apellido', required = False)
    telefono = forms.CharField(label='Cambiar telefono', required = False)
    biografia = forms.CharField(max_length=300, required=False, widget=forms.Textarea)
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'telefono', 'biografia', 'avatar']



