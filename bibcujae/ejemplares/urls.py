from rest_framework import routers
from django.urls import path, include

from .api import EjemplarViewSet
from .views import *

router = routers.DefaultRouter()
router.register(r'ejemplar', EjemplarViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/document/ejemplar/create', crear_ejemplar, name='create-ejemplar'),
    path('api/document/ejemplar/update/<int:ejemplar_id>', actualizar_ejemplar, name='update-ejemplar'),
    path('api/document/ejemplar/all', obtener_ejemplares, name='get-all-ejemplares'),
    path('api/document/ejemplar/libro/<int:libro_id>', obtener_ejemplares_de_libro, name='get-ejemplares-of-book'),
    path('api/document/ejemplar/<int:ejemplar_id>', eliminar_ejemplar, name='delete-ejemplar'),
    path('api/document/ejemplar/filter/', obtener_ejemplar_con_filtros, name='get-ejemplar-with-filter'),

    # path('api/document/materia/name', getMateriasByName, name='get-materias-by-name'),
]
