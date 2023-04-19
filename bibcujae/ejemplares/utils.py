import io
import random
import base64
from barcode import EAN13
from io import BytesIO
from PIL import Image

from barcode.writer import ImageWriter
from django.http import JsonResponse
from .models import Ejemplar


def generate_barcode(code):
    # Tomar solo los primeros 12 caracteres del código
    code_str = str(code)[:12]
    # Crear un objeto de código de barras EAN-13
    ean = EAN13(code_str, writer=ImageWriter())

    # Guardar el código de barras como una imagen en un objeto BytesIO
    buffer = io.BytesIO()
    ean.write(buffer)

    # Obtener el código a partir del objeto EAN13
    code = ean.get_fullcode()
    # Devolver el valor del código de barras y la imagen
    return code, buffer.getvalue()


def barCodeView(value):
    # Generar el código de barras
    codeValue, codeImage = generate_barcode(value)

    # Crear una respuesta JSON que contenga el valor del código y la imagen
    return {
        'codeValue': codeValue,
        'codeImage': base64.b64encode(codeImage).decode('utf-8')
    }


def barcodeImageView(valor):
    # Generar el código de barras
    resp = barCodeView(valor)
    valor_codigo = resp.get('codeValue')
    imagen_codigo = resp.get('codeImage')
    print(valor_codigo)

    return {'codeValue': valor_codigo, 'codeImage': imagen_codigo}


def generar_codigo_barras_unico():
    codigo_barras = None
    while not codigo_barras:
        num_aleatorio = random.randint(100000000000, 999999999999)
        if not Ejemplar.objects.filter(cod_barras=num_aleatorio).exists():
            codigo_barras = num_aleatorio
    return codigo_barras
