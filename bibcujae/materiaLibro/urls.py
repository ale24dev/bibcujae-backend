from rest_framework import routers
from django.urls import path, include

from .api import MateriaLibroViewSet
from .views import *

router = routers.DefaultRouter()
router.register(r'materiaLibro', MateriaLibroViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/document/materia-libro/booksByMateria', getBooksByMaterias, name='get-books-by-materias'),
]
