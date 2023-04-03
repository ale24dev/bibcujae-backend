from django.shortcuts import render
from django.db.models import Q
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes

from .models import MateriaLibro

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def getBooksByMaterias(request):
    if request.method == 'GET':
        materiaLibros = MateriaLibro.objects.all()
        materiaLibro_list = [materiaLibro.to_dict() for materiaLibro in materiaLibros]
        return Response(materiaLibro_list)