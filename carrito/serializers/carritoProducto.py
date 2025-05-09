from rest_framework import serializers
from .carrito import Carrito


class CarritoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = '__all__'
