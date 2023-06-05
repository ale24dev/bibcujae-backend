from .models import Ejemplar
from rest_framework import viewsets, permissions
from .serializers import EjemplarSerializer

class EjemplarViewSet(viewsets.ModelViewSet):
    queryset = Ejemplar.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EjemplarSerializer