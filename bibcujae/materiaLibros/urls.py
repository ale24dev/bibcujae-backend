from rest_framework import routers
from django.urls import path, include

from .api import MateriaLibrosViewSet
from .views import *

router = routers.DefaultRouter()
router.register(r'materiaLibros', MateriaLibrosViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/document/materia-libro/booksByMateria', getBooksByMaterias, name='get-books-by-materias'),
    path('api/document/materia-libro/materiasByBook', getMateriasByBook, name='get-materias-by-book'),
]
