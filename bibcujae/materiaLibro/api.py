from .models import MateriaLibros
from rest_framework import viewsets, permissions
from .serializers import MateriaLibrosSerializer

class MateriaLibrosViewSet(viewsets.ModelViewSet):
    queryset = MateriaLibros.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MateriaLibrosSerializer