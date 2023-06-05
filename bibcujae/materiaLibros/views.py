from django.shortcuts import render
from django.db.models import Q
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes

from book.models import Book
from .models import MateriaLibros
from materia.models import Materia
# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def getBooksByMaterias(request):
    if request.method == 'GET':
        materia_id = request.GET.get('id')
        materia = get_object_or_404(Materia, materia_id=materia_id)

        materiaLibros = MateriaLibros.objects.filter(materia_id=materia.materia_id)

        materiaLibro_list = [materiaLibro.to_dict() for materiaLibro in materiaLibros]
        return Response(materiaLibro_list)
    
@api_view(['GET'])
@permission_classes([AllowAny])
def getMateriasByBook(request):
    if request.method == 'GET':
        libro_id = request.GET.get('id')
        book = get_object_or_404(Book, libro_id=libro_id)

        materiaLibros = MateriaLibros.objects.filter(libro_id=book.libro_id)

        materiaLibro_list = [materiaLibro.to_dict() for materiaLibro in materiaLibros]
        return Response(materiaLibro_list)