import json
from django.db.models import Q
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes

from .models import Book, bookFromJson, parseParams

@api_view(['GET'])
@permission_classes([AllowAny])
def getAllBooks(request):
    if request.method == 'GET':
        books = Book.objects.all()
        books_list = [book.to_dict() for book in books]
        return Response(books_list)


@api_view(['GET'])
@permission_classes([AllowAny])
def getBookWithFilter(request):
    if request.method == 'GET':
        filtro = parseParams(request)

       # Construir la consulta de filtrado
        query = Q()
        for key, value in filtro.items():
            if value is not None:
                query &= Q(**{key: value})

        # Aplicar el filtro a la lista de libros
        listBooks = Book.objects.filter(query)
        books_list = [book.to_dict() for book in listBooks]
        return Response(books_list)


@api_view(['GET'])
@permission_classes([AllowAny])
def getBookByDomCode(request, domCode):
    if request.method == 'GET':
        book = get_object_or_404(Book, cod_domicilio=domCode)
        bookAux = book.to_dict()
        return Response(bookAux)


@api_view(['POST'])
@permission_classes([AllowAny])
def createBook(request):
    data = json.loads(request.body)

    if request.method == 'POST':
        book = bookFromJson(data)
        book_dict = book.to_dict()
        book.save()
    return Response(book_dict)


@api_view(['PATCH'])
@permission_classes([AllowAny])
def updateBook(request, id):
    data = json.loads(request.body)

    if request.method == 'PATCH':
        bookAux = bookFromJson(data)
        book = Book.objects.get(libro_id=id)

        for attr, value in vars(bookAux).items():
            if value is not None:
                setattr(book, attr, value)

        book.save()
        
    book_dict = book.to_dict()
    return Response(book_dict)
