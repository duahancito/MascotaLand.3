#Nos va a permitir cenvertir la data

from .models import *
from rest_framework import serializers

class TipoProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = '__all__'

class ProductoSerializers(serializers.ModelSerializer):
    tipo = TipoProductoSerializers(read_only=True)
    class Meta:
        model = Producto
        fields = '__all__'


