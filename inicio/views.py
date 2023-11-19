from django.shortcuts import render, redirect, HttpResponse
from inicio.forms import LlaveroFormulario
from inicio.forms import SoporteCelularesFormulario
from inicio.forms import PortaMemoriasFormulario
from inicio.forms import ActualizarLlaveroFormulario
from inicio.forms import ActualizarPortaMemoriasFormulario
from inicio.forms import ActualizarSoporteCelularesFormulario
from inicio.models import SoporteCelulares
from inicio.models import Llaveros
from django.http import Http404, HttpResponse
from inicio.models import PortaMemorias
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser



    # v3  
def inicio(request):   
    return render(request, 'inicio/inicio.html',{})

def about(request):   
    return render(request, 'inicio/about.html',{})





@login_required    
def carrito (request):
    if request.user.is_authenticated:
        
        modelo_a_buscar = request.GET.get('modelo', '')
    
        if modelo_a_buscar:
            listado_en_carrito = list(Llaveros.objects.filter(modelo__icontains=modelo_a_buscar, usuario=request.user)) + list(PortaMemorias.objects.filter(modelo__icontains=modelo_a_buscar, usuario=request.user)) + list(SoporteCelulares.objects.filter(modelo__icontains=modelo_a_buscar, usuario=request.user))
        else:
    
         listado_en_carrito = list(Llaveros.objects.filter(modelo__icontains=modelo_a_buscar, usuario=request.user)) + list(PortaMemorias.objects.filter(modelo__icontains=modelo_a_buscar, usuario=request.user)) + list(SoporteCelulares.objects.filter(modelo__icontains=modelo_a_buscar, usuario=request.user))
        
    else:
        listado_en_carrito = Llaveros.objects.filter(modelo__icontains=modelo_a_buscar, usuario=request.user) + PortaMemorias.objects.filter(modelo__icontains=modelo_a_buscar, usuario=request.user) + SoporteCelulares.objects.filter(modelo__icontains=modelo_a_buscar, usuario=request.user)
    
    return render(request, 'inicio/carrito.html', {'listado_en_carrito': listado_en_carrito})







def pedido_de_llaveros(request):
    
    print(request.POST)
    
    if request.method == 'POST':
        
        if isinstance(request.user, AnonymousUser):
        
            return redirect('login') 
    
        formulario = LlaveroFormulario(request.POST)
        if formulario.is_valid():
            infor_limpia = formulario.cleaned_data
            
            modelo = infor_limpia.get('modelo')
            descripcion = infor_limpia.get('descripcion')
            color = infor_limpia.get('color')
            cantidad = infor_limpia.get('cantidad')
            
            

            llavero = Llaveros(modelo=modelo, descripcion=descripcion, color=color, cantidad=cantidad, usuario=request.user)
            llavero.save()

            return redirect('carrito')
        else:
            return render(request, 'inicio/pedido_de_llaveros.html', {'formulario': formulario})
    else:
        formulario = LlaveroFormulario()
        return render(request, 'inicio/pedido_de_llaveros.html', {'formulario': formulario})








    
def pedido_de_porta_memorias (request):
    
    
    
    print(request.POST)
       

    if request.method =='POST':
        
        if isinstance(request.user, AnonymousUser):
        
            return redirect('login') 
        
        formulario = PortaMemoriasFormulario(request.POST)
        if formulario.is_valid():
            infor_limpia = formulario.cleaned_data
            
            modelo = infor_limpia.get('modelo')
            descripcion = infor_limpia.get('descripcion')
            color = infor_limpia.get('color')
            cantidad = infor_limpia.get('cantidad')
            
            porta_memorias = PortaMemorias(modelo=modelo, descripcion=descripcion, color=color, cantidad=cantidad, usuario=request.user)
            porta_memorias.save()
            
            return redirect('carrito')
        else: 
            return render(request, 'inicio/pedido_de_porta_memorias.html', {'formulario': formulario})
            
        
    formulario = PortaMemoriasFormulario()
    return render(request, 'inicio/pedido_de_porta_memorias.html', {'formulario': formulario})    




def pedido_de_soporte_para_celulares (request):
    
    print(request.POST)
       

    if request.method =='POST':
        
        if isinstance(request.user, AnonymousUser):
        
            return redirect('login') 
        
        formulario = SoporteCelularesFormulario(request.POST)
        if formulario.is_valid():
            infor_limpia = formulario.cleaned_data
            
            modelo = infor_limpia.get('modelo')
            descripcion = infor_limpia.get('descripcion')
            color = infor_limpia.get('color')
            cantidad = infor_limpia.get('cantidad')
            
            soporte_para_celulares = SoporteCelulares(modelo=modelo, descripcion=descripcion, color=color, cantidad=cantidad, usuario=request.user)
            soporte_para_celulares.save()
            
            return redirect('carrito')
        else: 
            return render(request, 'inicio/pedido_de_soporte_para_celulares.html', {'formulario': formulario})
            
        
    formulario = SoporteCelularesFormulario()
    return render(request, 'inicio/pedido_de_soporte_para_celulares.html', {'formulario': formulario})






@login_required
def eliminar_pedido(request, carrito_id1):
    try:
        pedido_a_eliminar1 = Llaveros.objects.get(id=carrito_id1)
        pedido_a_eliminar1.delete()
    except Llaveros.DoesNotExist:
        try:
            pedido_a_eliminar1 = PortaMemorias.objects.get(id=carrito_id1)
            pedido_a_eliminar1.delete()
        except PortaMemorias.DoesNotExist:
            try:
                pedido_a_eliminar1 = SoporteCelulares.objects.get(id=carrito_id1)
                pedido_a_eliminar1.delete()
            except SoporteCelulares.DoesNotExist:
               
                pass
    
    return redirect('carrito')


@login_required
def actualizar_pedido(request, carrito_id1):
    try:
        pedido_a_actualizar = Llaveros.objects.get(id=carrito_id1)
        formulario = ActualizarLlaveroFormulario()
    except Llaveros.DoesNotExist:
        try:
            pedido_a_actualizar = PortaMemorias.objects.get(id=carrito_id1)
            formulario = ActualizarPortaMemoriasFormulario()
        except PortaMemorias.DoesNotExist:
            try:
                pedido_a_actualizar = SoporteCelulares.objects.get(id=carrito_id1)
                formulario = ActualizarSoporteCelularesFormulario()
            except SoporteCelulares.DoesNotExist:
                return HttpResponse("Pedido no encontrado")

    if request.method == "POST":
        if isinstance(pedido_a_actualizar, Llaveros):
            formulario = ActualizarLlaveroFormulario(request.POST)
        elif isinstance(pedido_a_actualizar, PortaMemorias):
            formulario = ActualizarPortaMemoriasFormulario(request.POST)
        elif isinstance(pedido_a_actualizar, SoporteCelulares):
            formulario = ActualizarSoporteCelularesFormulario(request.POST)
        
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            pedido_a_actualizar.modelo = info_nueva.get('modelo')
            pedido_a_actualizar.descripcion = info_nueva.get('descripcion')
            pedido_a_actualizar.color = info_nueva.get('color')
            pedido_a_actualizar.cantidad = info_nueva.get('cantidad')
            pedido_a_actualizar.save()
            return redirect('carrito')
    
    else:
        initial_data = {
            'modelo': pedido_a_actualizar.modelo,
            'descripcion': pedido_a_actualizar.descripcion,
            'cantidad': pedido_a_actualizar.cantidad,
            'color': pedido_a_actualizar.color
        }
        if isinstance(pedido_a_actualizar, Llaveros):
            formulario = ActualizarLlaveroFormulario(initial=initial_data)
        elif isinstance(pedido_a_actualizar, PortaMemorias):
            formulario = ActualizarPortaMemoriasFormulario(initial=initial_data)
        elif isinstance(pedido_a_actualizar, SoporteCelulares):
            formulario = ActualizarSoporteCelularesFormulario(initial=initial_data)
    
    return render(request, 'inicio/actualizar_pedido.html', {'formulario': formulario})





@login_required
def detalle_pedido(request, carrito_id1):
    try:
        detalles = Llaveros.objects.get(id=carrito_id1)
    except Llaveros.DoesNotExist:
        try:
            detalles = PortaMemorias.objects.get(id=carrito_id1)
        except PortaMemorias.DoesNotExist:
            try:
                detalles = SoporteCelulares.objects.get(id=carrito_id1)
            except SoporteCelulares.DoesNotExist:
                raise Http404("El pedido no se encontró")

    return render(request, 'inicio/detalle_pedido.html', {"detalles": detalles})
