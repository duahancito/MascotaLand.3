from django.urls import path, include
from .views import *
from rest_framework import routers

#Creamos las listas del API

router = routers.DefaultRouter()
router.register('productos', ProductoViewset)
router.register('tipoproductos', TipoProductoViewset)


urlpatterns = [
    #API
    path('api/', include(router.urls)),
    #RUTAS
    path('', index, name="index"),
    path('indexapi/', indexapi, name="indexapi"),
    path('about/', about, name="about"),
    path('blog/', blog, name="blog"),
    path('contact/', contact, name="contact"),
    path('detail/', detail, name="detail"),
    path('price/', price, name="price"),
    path('product/', product, name="product"),
    path('service/', service, name="service"),
    path('team/', team, name="team"),
    path('testimonial/', testimonial, name="testimonial"),
    path('rastreo/', rastreo, name="rastreo"), 
    path('pagocarro/', pagocarro, name="pagocarro"),
    path('register/', register, name="register"),
    #CRUD
    path('add/', add, name="add"),
    path('update/<id>/', update, name="update"),
    path('delete/<id>/', delete, name="delete"),
    #Carrito
    path('carrito/', carrito, name='carrito'),
    path('carrito/agregar/<int:producto_id>/',agregar_producto, name='agregar_producto'),
    path('carrito/eliminar/<int:item_id>/',eliminar_producto, name='eliminar_producto'),

]