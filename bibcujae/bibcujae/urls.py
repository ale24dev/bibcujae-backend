from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book.urls')),
    path('', include('materia.urls')),
    path('', include('materiaLibros.urls')),
    path('', include('authentication.urls')),
    path('', include('ejemplares.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
