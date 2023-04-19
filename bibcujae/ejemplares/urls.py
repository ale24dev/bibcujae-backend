from rest_framework import routers
from django.urls import path, include

from .api import EjemplarViewSet
from .views import *

router = routers.DefaultRouter()
router.register(r'ejemplar', EjemplarViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/document/ejemplar/create', crearEjemplar, name='create-ejemplar'),
    path('api/document/ejemplar/all', getAllEjemplares, name='get-all-ejemplares'),
    path('api/document/ejemplar/libro/<int:libro_id>', getEjemplaresOfBook, name='get-ejemplares-of-book'),
    # path('api/document/materia/name', getMateriasByName, name='get-materias-by-name'),
]
