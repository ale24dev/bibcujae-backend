from django.db import models
from datetime import datetime

from book.models import Book


class EstadoEjemplar(models.Model):
    estado_ejemplar_id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = "estado_ejemplar"

    def to_dict(self):
        return {
            'estado_ejemplar_id': self.estado_ejemplar_id,
            'estado': self.estado,
        }

class Ejemplar(models.Model):
    libro = models.ForeignKey(Book, on_delete=models.CASCADE)
    estado_ejemplar = models.ForeignKey(
        EstadoEjemplar, on_delete=models.CASCADE)
    ejemplar_id = models.AutoField(primary_key=True)
    cod_barras = models.CharField(max_length=20, null=True)
    subdivision1 = models.CharField(max_length=100, null=True)
    subdivision2 = models.CharField(max_length=100, null=True)
    no_ingreso = models.CharField(max_length=50, null=True)
    fecha_ingreso = models.DateField(null=True)
    ubicacion = models.CharField(max_length=100, null=True)
    via_adq = models.CharField(max_length=100, null=True)
    procedencia = models.CharField(max_length=100, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    
    

    class Meta:
        db_table = "ejemplar"

    def __str__(self):
        return f"{self.libro} - Ejemplar {self.ejemplar_id}"

    def to_dict(self, book_json):
        return {
            'libro': book_json,
            'ejemplar_id': self.ejemplar_id,
            'cod_barras': self.cod_barras,
            'subdivision1': self.subdivision1,
            'subdivision2': self.subdivision2,
            'no_ingreso': self.no_ingreso,
            'fecha_ingreso': self.fecha_ingreso,
            'ubicacion': self.ubicacion,
            'via_adq': self.via_adq,
            'procedencia': self.procedencia,
            'precio': self.precio if self.precio is not None else None,
            'estado_ejemplar':  self.estado_ejemplar.to_dict()
        }


def fromJson(json_data):
    # cod_barras = json_data.get('cod_barras')
    subdivision1 = json_data.get('subdivision1')
    subdivision2 = json_data.get('subdivision2')
    no_ingreso = json_data.get('no_ingreso')
    fecha_ingreso = datetime.strptime(
        json_data.get('fecha_ingreso'), '%Y-%m-%d %H:%M:%S').date()
    ubicacion = json_data.get('ubicacion')
    via_adq = json_data.get('via_adq')
    procedencia = json_data.get('procedencia')
    precio = json_data.get('precio')

    ejemplar = Ejemplar(
        libro=Book.objects.get(libro_id=json_data.get('libro_id')),
        # cod_barras=cod_barras,
        subdivision1=subdivision1,
        subdivision2=subdivision2,
        no_ingreso=no_ingreso,
        fecha_ingreso=fecha_ingreso,
        ubicacion=ubicacion,
        via_adq=via_adq,
        procedencia=procedencia,
        precio=precio,
    )
    return ejemplar


def parseParams(request):
    ejemplar_id = request.GET.get('ejemplar_id')
    cod_barras = request.GET.get('cod_barras')
    subdivision1 = request.GET.get('subdivision1')
    subdivision2 = request.GET.get('subdivision2')
    no_ingreso = request.GET.get('no_ingreso')
    fecha_ingreso = datetime.strptime(
        request.GET.get('fecha_ingreso'), '%Y-%m-%d').date() if request.GET.get('fecha_ingreso') is not None else None
    ubicacion = request.GET.get('ubicacion')
    via_adq = request.GET.get('via_adq')
    procedencia = request.GET.get('procedencia')
    precio = request.GET.get('precio')
    estado_ejemplar_id = request.GET.get('estado_ejemplar_id')

    return {
        'ejemplar_id': ejemplar_id,
        'cod_barras': cod_barras,
        'subdivision1': subdivision1,
        'subdivision2': subdivision2,
        'no_ingreso': no_ingreso,
        'fecha_ingreso': fecha_ingreso,
        'ubicacion': ubicacion,
        'via_adq': via_adq,
        'procedencia': procedencia,
        'precio': precio,
        # 'estado_ejemplar': EstadoEjemplar.objects.get(estado_ejemplar_id=estado_ejemplar_id)
        'estado_ejemplar_id': estado_ejemplar_id
    }
