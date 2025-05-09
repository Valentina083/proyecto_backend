"""
URL configuration for proyecto_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from carrito.views import agregar_producto
from carrito.views import CarritoViewSet
from productos.views import CategoriaViewSet
from productos.views import ProductoViewSet
from carrito.views import CarritoProductoViewSet

router = DefaultRouter()
router.register('carrito', CarritoViewSet, 'view_carrito')
router.register('categorias', CategoriaViewSet, 'view_categoria')
router.register('productos', ProductoViewSet, 'view_producto')
router.register('carritoproducto', CarritoProductoViewSet, 'view_carrito_producto')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('agregar_producto/', agregar_producto, name='agregar_producto'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
