import json
from django.db.models import Q
from django.http import HttpResponse
from barcode.writer import ImageWriter
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes

from .models import Book, bookFromJson, parseParams
from book.utils import customPagination, writeJsonToExcel


@api_view(['GET'])
@permission_classes([AllowAny])
def getAllBooks(request):
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
        book.save()
    return Response("El libro ha sido creado correctamente")


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


