from django.db import models
from productos.models import Producto


class Carrito(models.Model):
    session_id = models.CharField(max_length=100)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.producto.nombre} x{self.cantidad}"
