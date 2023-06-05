from .models import Materia
from rest_framework import viewsets, permissions
from .serializers import MateriaSerializer

class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MateriaSerializer