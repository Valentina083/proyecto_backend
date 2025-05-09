from rest_framework import viewsets
from carrito.models import CarritoProducto
from carrito.serializers import CarritoProductoSerializer


class CarritoProductoViewSet(viewsets.ModelViewSet):
    queryset = CarritoProducto.objects.all()
    serializer_class = CarritoProductoSerializer
