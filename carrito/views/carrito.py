from rest_framework import viewsets
from carrito.models import Carrito
from carrito.serializers import CarritoSerializer


class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer
