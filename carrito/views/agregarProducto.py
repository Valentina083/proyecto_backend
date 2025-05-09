from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from productos.models import Producto
from carrito.models import Carrito, CarritoProducto


@api_view(['POST'])
def agregar_producto(request):
    session_id = request.data.get('session_id')
    producto_id = request.data.get('producto_id')
    cantidad = request.data.get('cantidad', 1)

    if not all([session_id, producto_id]):
        return Response({"error": "Faltan datos obligatorios."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Obtener el producto
        producto = Producto.objects.get(id=producto_id)

        # Buscar el carrito del usuario (basado en session_id)
        carrito, created = Carrito.objects.get_or_create(session_id=session_id, estado='pendiente')

        # Si el producto ya está en el carrito, simplemente actualiza la cantidad
        carrito_producto, created = CarritoProducto.objects.get_or_create(
            carrito=carrito,
            producto=producto
        )
        carrito_producto.cantidad += cantidad  # Aumenta la cantidad
        carrito_producto.save()

        return Response({"mensaje": f"{producto.nombre} añadido al carrito."})

    except Producto.DoesNotExist:
        return Response({"error": "Producto no encontrado."}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
