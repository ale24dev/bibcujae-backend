import json
from django.db.models import Q
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes

from .models import Materia, parseParams

# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def getAllMaterias(request):
    if request.method == 'GET':
        materias = Materia.objects.all()
        materias_list = [materia.to_dict() for materia in materias]
        return Response(materias_list)


@api_view(['GET'])
@permission_classes([AllowAny])
def getMateriaById(request, id):
    if request.method == 'GET':
        materia = get_object_or_404(Materia, materia_id=id)
        return Response(materia.to_dict())


@api_view(['GET'])
@permission_classes([AllowAny])
def getMateriasByName(request):
    if request.method == 'GET':
        materia = parseParams(request)
        materias = Materia.objects.filter(
            name__startswith=materia["name"].upper())

        materias_list = [materia.to_dict() for materia in materias]
        return Response(materias_list)
