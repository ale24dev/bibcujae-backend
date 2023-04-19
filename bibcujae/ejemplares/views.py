import io
import json
import base64
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes

from .models import *
from .utils import *
# Create your views here.


@api_view(['GET'])
@permission_classes([AllowAny])
def getAllEjemplares(request):
    if request.method == 'GET':
        ejemplares = Ejemplar.objects.all()
        ejemplares_list = [ejemplar.to_dict() for ejemplar in ejemplares]
        return Response(ejemplares_list)


@api_view(['GET'])
@permission_classes([AllowAny])
def getEjemplaresOfBook(request, libro_id):
    if request.method == 'GET':
        book = get_object_or_404(Book, libro_id=libro_id)

        ejemplares = Ejemplar.objects.filter(libro_id=book.libro_id)

        ejemplares_list = [ejemplar.to_dict() for ejemplar in ejemplares]
        return Response(ejemplares_list)


@api_view(['POST'])
@permission_classes([AllowAny])
def crearEjemplar(request):
    data = json.loads(request.body)

    if request.method == 'POST':
        ejemplar = fromJson(data)

    code = generar_codigo_barras_unico()
    ejemplar.cod_barras = code

    response = barcodeImageView(code)

    codeValue = response.get("codeValue")
    codeImage = response.get("codeImage")

    # Almacenamos el codigo de barra generado en el ejemplar
    ejemplar.cod_barras = codeValue
    ejemplar.save()

    response = JsonResponse({'codeValue': codeValue, 'codeImage': codeImage})
    # Configurar la cabecera de la respuesta HTTP para que se muestre la imagen
    response['Content-Type'] = 'image/png'
    response['Content-Disposition'] = 'inline; filename="barcode.png"'

    response.content = base64.b64decode(codeImage)

    return response
    # return Response("200")
