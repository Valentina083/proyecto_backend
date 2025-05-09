from rest_framework import serializers
from productos.models import Producto


class ProductoSerializer(serializers.ModelSerializer):
    imagen = serializers.ImageField(use_url=True)

    class Meta:
        model = Producto
        fields = '__all__'
