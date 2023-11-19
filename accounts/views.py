from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from accounts.forms import MiFormularioDeCreacion, MiFormularioDeEdicionDePerfil
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from accounts.models import DatosExtra
from django.views import View
from django.shortcuts import render
from django.contrib.auth.models import User



def login (request):
    
    if request.method =='POST':
        formulario = AuthenticationForm(request, data=request.POST) 
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contrasenia)
            
            django_login (request, user)
            
            DatosExtra.objects.get_or_create(user=request.user)
    
    
            return redirect('inicio')
        
        else: 
            return render(request, 'accounts/login.html', {'formulario_de_login': formulario})
    
    formulario = AuthenticationForm() 
    return render(request, 'accounts/login.html', {'formulario_de_login': formulario})


def registro (request):
    formulario = MiFormularioDeCreacion()
    
    if request.method == 'POST':
        formulario = MiFormularioDeCreacion(request.POST)
        if formulario.is_valid():
            
            formulario.save()
            
            return redirect ('login')
        
        
    return render(request, 'accounts/registro.html', {'formulario_de_registro':formulario})








@login_required
def ver_perfil(request):
    
    
    
    user_details = {
        'nombre': request.user.first_name,
        'apellido': request.user.last_name,
        'email': request.user.email,
        'telefono': request.user.datosextra.telefono,
        'biografia': request.user.datosextra.biografia,
        'avatar': request.user.datosextra.avatar,
    }
    return render(request, 'accounts/perfil.html', {'detalles': user_details})




def editar_perfil(request):
    
    datos_extra = request.user.datosextra
    
    formulario = MiFormularioDeEdicionDePerfil(initial={'biografia': datos_extra.biografia, 'avatar': datos_extra.avatar, 'telefono': datos_extra.telefono}, instance=request.user)
    
    if request.method == 'POST':
        formulario = MiFormularioDeEdicionDePerfil(request.POST, request.FILES, instance=request.user)
        
        if formulario.is_valid():
            
            nueva_biografia = formulario.cleaned_data.get('biografia')
            nuevo_avatar = formulario.cleaned_data.get('avatar')
            nuevo_telefono = formulario.cleaned_data.get('telefono')
            
            if nueva_biografia:
                datos_extra.biografia = nueva_biografia
                
            if nuevo_avatar:    
                datos_extra.avatar = nuevo_avatar
                
            if nuevo_telefono:
                datos_extra.telefono = nuevo_telefono
                
            datos_extra.save()
            formulario.save()
            
            return redirect ('ver_perfil') 
             
          
        
    return render(request, 'accounts/editar_perfil.html', {'formulario': formulario})




class CambioPassword(PasswordChangeView):
    
    template_name = 'accounts/cambiar_password.html'
    
    success_url = reverse_lazy('ver_perfil') 