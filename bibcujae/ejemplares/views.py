import json
import base64
import cairo
from django.db.models import Q
from django.http import JsonResponse
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes

from .utils import *
from .models import *
from book.models import *


@api_view(['GET'])
@permission_classes([AllowAny])
def obtener_ejemplares(request):
    if request.method == 'GET':
        ejemplares = Ejemplar.objects.all()
        ejemplares_list = [ejemplar.to_dict() for ejemplar in ejemplares]
        return Response(ejemplares_list)


@api_view(['GET'])
@permission_classes([AllowAny])
def obtener_ejemplares_de_libro(request, libro_id):
    if request.method == 'GET':
        book = get_object_or_404(Book, libro_id=libro_id)

        ejemplares = Ejemplar.objects.filter(libro_id=book.libro_id)

        ejemplares_list = [ejemplar.to_dict(
            book.to_dict()) for ejemplar in ejemplares]
        return Response(ejemplares_list)


@api_view(['GET'])
@permission_classes([AllowAny])
def obtener_ejemplar_con_filtros(request):
    if request.method == 'GET':
        filtro = parseParams(request)

       # Construir la consulta de filtrado
        query = Q()
        for key, value in filtro.items():
            if value is not None:
                query &= Q(**{key: value})

        # Aplicar el filtro a la lista de libros
        listEjemplares = Ejemplar.objects.filter(query)
        ejemplares_list = [ejemplar.to_dict() for ejemplar in listEjemplares]
        return Response(ejemplares_list)


@api_view(['POST'])
@permission_classes([AllowAny])
def crear_ejemplar(request):
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
    ejemplar.estado_ejemplar = EstadoEjemplar.objects.get(
        estado='inventario')
    ejemplar.save()

    response = JsonResponse({'codeValue': codeValue, 'codeImage': codeImage})
    # Configurar la cabecera de la respuesta HTTP para que se muestre la imagen
    response['Content-Type'] = 'image/png'
    response['Content-Disposition'] = 'inline; filename="barcode.png"'

    response.content = base64.b64decode(codeImage)

    return response
    # return Response("200")

@api_view(['DELETE'])
@permission_classes([AllowAny])
def eliminar_ejemplar(request, ejemplar_id):
    ejemplar = get_object_or_404(Ejemplar, ejemplar_id=ejemplar_id)
    if request.method == 'DELETE':
        ejemplar.delete()

        return JsonResponse({"response": "Ejemplar eliminado correctamente"})
    
@api_view(['PATCH'])
@permission_classes([AllowAny])
def actualizar_ejemplar(request, ejemplar_id):
     if request.method == 'PATCH':
        ejemplar = get_object_or_404(Ejemplar, ejemplar_id=ejemplar_id)
        
        data = json.loads(request.body)
        
        ejemplar.subdivision1 = data.get('subdivision1', ejemplar.subdivision1)
        ejemplar.subdivision2 = data.get('subdivision2', ejemplar.subdivision2)
        ejemplar.no_ingreso = data.get('no_ingreso', ejemplar.no_ingreso)
        ejemplar.fecha_ingreso = datetime.strptime(data.get('fecha_ingreso'), '%Y-%m-%d %H:%M:%S').date() if 'fecha_ingreso' in data else ejemplar.fecha_ingreso
        ejemplar.ubicacion = data.get('ubicacion', ejemplar.ubicacion)
        ejemplar.via_adq = data.get('via_adq', ejemplar.via_adq)
        ejemplar.procedencia = data.get('procedencia', ejemplar.procedencia)
        ejemplar.precio = data.get('precio', ejemplar.precio)

        ejemplar.save()
        
        return JsonResponse({"response": "Ejemplar actualizado correctamente"})
    
# def imprimir_imagen_bytes(imagen_bytes):
#     # Convertir los bytes en un objeto Image
#     imagen = Image.open(BytesIO(imagen_bytes))

#     # Configurar la impresora
#     conexion_impresora = cups.Connection()
#     impresoras = conexion_impresora.getPrinters()
#     impresora_nombre = list(impresoras.keys())[0]  # Usar la primera impresora encontrada
#     impresora = conexion_impresora.getPrinterAttributes(impresora_nombre)
#     ancho, alto, margen_x, margen_y = impresora['media-bottom-margin'], impresora['media-right-margin'], impresora['printer-margins'][0], impresora['printer-margins'][1]
#     orientacion = cairo.LANDSCAPE if imagen.width > imagen.height else cairo.PORTRAIT
#     surface = cairo.PSSurface("/dev/usb/lp0", orientacion, (ancho, alto))
#     surface.set_device_offset(margen_x, margen_y)
#     context = cairo.Context(surface)

#     # Dibujar la imagen en el surface
#     context.set_source_rgb(1, 1, 1)  # Fondo blanco
#     context.rectangle(0, 0, ancho, alto)
#     context.fill()
#     context.set_source_surface(cairo.ImageSurface.create_from_png(BytesIO(imagen_bytes)), 0, 0)
#     context.paint()

#     # Imprimir la imagen
#     surface.finish()
