from django.urls import path
from inicio.views import inicio, carrito, productos, pedido_de_llaveros, pedido_de_porta_memorias, pedido_de_soporte_para_celulares


urlpatterns = [
    path('', inicio, name='inicio'),
    path('carrito/', carrito, name='carrito'),
    path('productos/', productos, name='productos'),
    path('pedido_de_llaveros/', pedido_de_llaveros, name='pedido_de_llaveros'),
    path('pedido_de_porta_memorias/', pedido_de_porta_memorias, name='pedido_de_porta_memorias'),
    path('pedido_de_soporte_para_celulares/', pedido_de_soporte_para_celulares, name='pedido_de_soporte_para_celulares'),
    
]