from django.urls import path
<<<<<<< HEAD
from inicio.views import inicio, carrito, productos, pedido_de_llaveros, pedido_de_porta_memorias, pedido_de_soporte_para_celulares
=======
from inicio.views import inicio, carrito, pedido_de_llaveros, pedido_de_porta_memorias, pedido_de_soporte_para_celulares
>>>>>>> 1cbed0cd986d84e4d55170048acd85f3add4d82e


urlpatterns = [
    path('', inicio, name='inicio'),
    path('carrito/', carrito, name='carrito'),
<<<<<<< HEAD
    path('productos/', productos, name='productos'),
=======
>>>>>>> 1cbed0cd986d84e4d55170048acd85f3add4d82e
    path('pedido_de_llaveros/', pedido_de_llaveros, name='pedido_de_llaveros'),
    path('pedido_de_porta_memorias/', pedido_de_porta_memorias, name='pedido_de_porta_memorias'),
    path('pedido_de_soporte_para_celulares/', pedido_de_soporte_para_celulares, name='pedido_de_soporte_para_celulares'),
    
]