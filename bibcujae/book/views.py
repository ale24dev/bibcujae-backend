import json
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from barcode.writer import ImageWriter
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes

from .models import Book, bookFromJson, parseParams
from typing import List, Dict
from book.utils import customPagination, writeJsonToExcel, validateFilters


@api_view(['GET'])
@permission_classes([AllowAny])
def getBookById(request, libro_id):
    if request.method == 'GET':
        book = get_object_or_404(Book, libro_id=libro_id)
        bookAux = book.to_dict()
        return Response(bookAux)


@api_view(['GET'])
@permission_classes([AllowAny])
def getBooksWithPag(request):
    # Set the number of items per page
    items_per_page = request.query_params.get('items')

    # Get the requested page number from the request query parameters
    page_number = request.query_params.get('page')

    # Get all the books from the database, ordered by id
    books = Book.objects.order_by('libro_id')

    # Paginate the results using the custom pagination class
    paginator = customPagination()
    paginator.page_size = items_per_page
    paginated_books = paginator.paginate_queryset(books, request)

    # Serialize the paginated books
    books_list = [book.to_dict() for book in paginated_books]

    # Return the serialized books with pagination metadata
    return paginator.get_paginated_response(books_list)


@api_view(['GET'])
@permission_classes([AllowAny])
def getAllBooks(request):
    if request.method == 'GET':
        books = Book.objects.all()
        books_list = [book.to_dict() for book in books]
        return Response(books_list)


@api_view(['POST'])
@permission_classes([AllowAny])
def writeInExcel(request):
    if request.method == 'POST':

        json_data = json.loads(request.body)
        data = request.body.decode('utf-8')
        json_data = json.loads(data)

        # for item in json_data:
        #     book = bookFromJson(item)
        #     book_dict = book.to_dict()
        # write_json_to_excel(book_dict, output_file)
        # write_json_to_excel(json_data, output_file)
        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="data.xlsx"'
        writeJsonToExcel(json_data, response)
        return response


@api_view(['POST'])
@permission_classes([AllowAny])
def getBookWithFilter(request):

    search_filters = json.loads(request.body)['searchFilters']
    query = Q()
    for sf in search_filters:
        resp = validateFilters(sf)
        if (resp is not None):
            return HttpResponse(resp, status=500)
        if sf['option'] == 'exact':
            query &= Q(**{sf['category']: sf['value']})
        elif sf['option'] == 'contains':
            query &= Q(**{sf['category'] + '__icontains': sf['value']})
        elif sf['option'] == 'range':
            values = sf['value'].split(',')
            query &= Q(**{sf['category'] + '__gte': values[0],
                       sf['category'] + '__lte': values[1]})
        elif sf['option'] == 'less_than':
            query &= Q(**{sf['category'] + '__lt': sf['value']})
        elif sf['option'] == 'greater_than':
            print("entreeee")
            query &= Q(**{sf['category'] + '__gt': sf['value']})

    books = Book.objects.filter(query)

    # Set the number of items per page
    items_per_page = request.query_params.get('items')

    # Get the requested page number from the request query parameters
    page_number = request.query_params.get('page')

    # Paginate the results using the custom pagination class
    paginator = customPagination()
    paginator.page_size = items_per_page
    paginated_books = paginator.paginate_queryset(books, request)

    # Serialize the paginated books
    books_list = [book.to_dict() for book in paginated_books]

    # Return the serialized books with pagination metadata
    return paginator.get_paginated_response(books_list)

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
        book.save()
    return Response("El libro ha sido creado correctamente")


@api_view(['PATCH'])
@permission_classes([AllowAny])
def updateBook(request, libro_id):
    if request.method == 'PATCH':
        libro = get_object_or_404(Book, libro_id=libro_id)

        data = json.loads(request.body)

        libro.titulo = data.get('titulo', libro.titulo)
        libro.entrada = data.get('entrada', libro.entrada)
        libro.tipo_autor = data.get('tipo_autor', libro.tipo_autor)
        libro.autor = data.get('autor', libro.autor)
        libro.otros_autores = data.get('otros_autores', libro.otros_autores)
        libro.edicion = data.get('edicion', libro.edicion)
        libro.serie = data.get('serie', libro.serie)
        libro.notas = data.get('notas', libro.notas)
        libro.anno_pub = data.get('anno_pub', libro.anno_pub)
        libro.mencion_resp = data.get('mencion_resp', libro.mencion_resp)
        libro.cod_domicilio = data.get('cod_domicilio', libro.cod_domicilio)
        libro.isbn = data.get('isbn', libro.isbn)
        libro.dewey = data.get('dewey', libro.dewey)
        libro.evento = data.get('evento', libro.evento)
        libro.otros_eventos = data.get('otros_eventos', libro.otros_eventos)
        libro.publicacion = data.get('publicacion', libro.publicacion)
        libro.colacion = data.get('colacion', libro.colacion)
        libro.otros_titulos = data.get('otros_titulos', libro.otros_titulos)
        libro.folleto = data.get('folleto', libro.folleto)
        libro.referencia = data.get('referencia', libro.referencia)
        libro.letras_ent = data.get('letras_ent', libro.letras_ent)
        libro.letra_titulo = data.get('letra_titulo', libro.letra_titulo)
        libro.clasif = data.get('clasif', libro.clasif)
        libro.idioma = data.get('idioma', libro.idioma)
        libro.pais = data.get('pais', libro.pais)

        libro.save()

        return JsonResponse({"response": "Libro actualizado correctamente"})


@api_view(['DELETE'])
@permission_classes([AllowAny])
def deleteBook(request, libro_id):
    book = get_object_or_404(Book, libro_id=libro_id)
    if request.method == 'DELETE':
        book.delete()

        return JsonResponse({"response": "Libro eliminado correctamente"})
