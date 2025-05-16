from rest_framework import serializers
from facturas.models import Factura, DetalleFactura


class DetalleFacturaSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source='producto.nombre', read_only=True)

    class Meta:
        model = DetalleFactura
        fields = ['producto', 'producto_nombre', 'cantidad', 'precio']


class FacturaSerializer(serializers.ModelSerializer):
    detalles = DetalleFacturaSerializer(source='detallefactura_set', many=True, read_only=True)
    cliente_nombre = serializers.CharField(source='cliente.nombre', read_only=True)

    class Meta:
        model = Factura
        fields = ['id', 'cliente_nombre', 'fecha', 'total', 'detalles']
