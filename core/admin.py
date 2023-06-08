from django.contrib import admin
from .models import *
# Register your models here.


# DEJA EN MODO TABLA LA VISUALIZACION EN EL ADMIN
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','stock','descripcion','tipo','vigente']
    search_fields = ['nombre']
   

admin.site.register(TipoProducto)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Carrito)
admin.site.register(ItemCarrito)