from django.urls import path
from inicio.views import inicio, carrito, pedido_de_llaveros, pedido_de_porta_memorias, pedido_de_soporte_para_celulares, eliminar_pedido, actualizar_pedido, detalle_pedido, about

urlpatterns = [
    path('', inicio, name='inicio'),
    path('carrito/', carrito, name='carrito'),
    path('pedido_de_llaveros/', pedido_de_llaveros, name='pedido_de_llaveros'),
    path('pedido_de_porta_memorias/', pedido_de_porta_memorias, name='pedido_de_porta_memorias'),
    path('pedido_de_soporte_para_celulares/', pedido_de_soporte_para_celulares, name='pedido_de_soporte_para_celulares'),
    path('eliminar_pedido/<int:carrito_id1>/', eliminar_pedido, name='eliminar_pedido'),
    path('actualizar_pedido/<int:carrito_id1>/', actualizar_pedido, name='actualizar_pedido'),
    path('detalle_pedido/<int:carrito_id1>/', detalle_pedido, name='detalle_pedido'),
    path('about/', about, name='about'),
   
]