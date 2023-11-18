from django.shortcuts import render, redirect
from inicio.forms import LlaveroFormulario
from inicio.forms import SoporteCelularesFormulario
from inicio.forms import PortaMemoriasFormulario
from inicio.models import SoporteCelulares
from inicio.models import Llaveros
from inicio.models import PortaMemorias




    # v3  
def inicio(request):   
    return render(request, 'inicio/inicio.html',{})

<<<<<<< HEAD
def productos(request):   
    return render(request, 'inicio/productos.html',{})
=======
>>>>>>> 1cbed0cd986d84e4d55170048acd85f3add4d82e


def carrito (request):
    
    modelo_a_buscar = request.GET.get('modelo')
    
    if modelo_a_buscar:
        listado_en_carrito = list(Llaveros.objects.filter(modelo__icontains=modelo_a_buscar)) + list(PortaMemorias.objects.filter(modelo__icontains=modelo_a_buscar)) + list(SoporteCelulares.objects.filter(modelo__icontains=modelo_a_buscar))
    else:
    
        listado_en_carrito = list(Llaveros.objects.all()) + list(PortaMemorias.objects.all()) + list(SoporteCelulares.objects.all())
    
    return render(request, 'inicio/carrito.html', {'listado_en_carrito': listado_en_carrito})






def pedido_de_llaveros (request):
    
    print(request.POST)
       

    if request.method =='POST':
        formulario = LlaveroFormulario(request.POST)
        if formulario.is_valid():
            infor_limpia = formulario.cleaned_data
            
            modelo = infor_limpia.get('modelo')
<<<<<<< HEAD
            descripcion = infor_limpia.get('descripcion')
            color = infor_limpia.get('color')
            cantidad = infor_limpia.get('cantidad')
            
            llavero = Llaveros(modelo=modelo, descripcion=descripcion, color=color, cantidad=cantidad)
=======
            descripción = infor_limpia.get('descripción')
            color = infor_limpia.get('color')
            cantidad = infor_limpia.get('cantidad')
            
            llavero = Llaveros(modelo=modelo, descripción=descripción, color=color, cantidad=cantidad)
>>>>>>> 1cbed0cd986d84e4d55170048acd85f3add4d82e
            llavero.save()
            
            return redirect('carrito')
        else: 
            return render(request, 'inicio/pedido_de_llaveros.html', {'formulario': formulario})
            
        
    formulario = LlaveroFormulario()
    return render(request, 'inicio/pedido_de_llaveros.html', {'formulario': formulario})


    
def pedido_de_porta_memorias (request):
    
    print(request.POST)
       

    if request.method =='POST':
        formulario = PortaMemoriasFormulario(request.POST)
        if formulario.is_valid():
            infor_limpia = formulario.cleaned_data
            
            modelo = infor_limpia.get('modelo')
<<<<<<< HEAD
            descripcion = infor_limpia.get('descripcion')
            color = infor_limpia.get('color')
            cantidad = infor_limpia.get('cantidad')
            
            porta_memorias = PortaMemorias(modelo=modelo, descripcion=descripcion, color=color, cantidad=cantidad)
=======
            descripción = infor_limpia.get('descripción')
            color = infor_limpia.get('color')
            cantidad = infor_limpia.get('cantidad')
            
            porta_memorias = PortaMemorias(modelo=modelo, descripción=descripción, color=color, cantidad=cantidad)
>>>>>>> 1cbed0cd986d84e4d55170048acd85f3add4d82e
            porta_memorias.save()
            
            return redirect('carrito')
        else: 
            return render(request, 'inicio/pedido_de_porta_memorias.html', {'formulario': formulario})
            
        
    formulario = PortaMemoriasFormulario()
    return render(request, 'inicio/pedido_de_porta_memorias.html', {'formulario': formulario})    

 
def pedido_de_soporte_para_celulares (request):
    
    print(request.POST)
       

    if request.method =='POST':
        formulario = SoporteCelularesFormulario(request.POST)
        if formulario.is_valid():
            infor_limpia = formulario.cleaned_data
            
            modelo = infor_limpia.get('modelo')
<<<<<<< HEAD
            descripcion = infor_limpia.get('descripcion')
            color = infor_limpia.get('color')
            cantidad = infor_limpia.get('cantidad')
            
            llavero = SoporteCelulares(modelo=modelo, descripcion=descripcion, color=color, cantidad=cantidad)
=======
            descripción = infor_limpia.get('descripción')
            color = infor_limpia.get('color')
            cantidad = infor_limpia.get('cantidad')
            
            llavero = SoporteCelulares(modelo=modelo, descripción=descripción, color=color, cantidad=cantidad)
>>>>>>> 1cbed0cd986d84e4d55170048acd85f3add4d82e
            llavero.save()
            
            return redirect('carrito')
        else: 
            return render(request, 'inicio/pedido_de_soporte_para_celulares.html', {'formulario': formulario})
            
        
    formulario = SoporteCelularesFormulario()
    return render(request, 'inicio/pedido_de_soporte_para_celulares.html', {'formulario': formulario})