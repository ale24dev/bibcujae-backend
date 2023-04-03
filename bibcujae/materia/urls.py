from rest_framework import routers
from django.urls import path, include

from .api import MateriaViewSet
from .views import *

router = routers.DefaultRouter()
router.register(r'book', MateriaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/document/materia/all', getAllMaterias, name='get-all-materias'),
    path('api/document/materia/id/<int:id>', getMateriaById, name='get-materia-by-id'),
    path('api/document/materia/name', getMateriasByName, name='get-materias-by-name'),
]
