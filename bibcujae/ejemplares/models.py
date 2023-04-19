from django.db import models
from datetime import datetime

from book.models import Book


class Ejemplar(models.Model):
    libro = models.ForeignKey(Book, on_delete=models.CASCADE)
    ejemplar_id = models.AutoField(primary_key=True)
    cod_barras = models.CharField(max_length=20, null=True)
    subdivision1 = models.CharField(max_length=100, null=True)
    subdivision2 = models.CharField(max_length=100, null=True)
    no_ingreso = models.CharField(max_length=50, null=True)
    fecha_ingreso = models.DateField(null=True)
    ubicacion = models.CharField(max_length=100, null=True)
    vias_adq = models.CharField(max_length=100, null=True)
    procedencia = models.CharField(max_length=100, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    class Meta:
        db_table = "ejemplar"

    def __str__(self):
        return f"{self.libro} - Ejemplar {self.ejemplar_id}"

    def to_dict(self):
        return {
            'libro_id': self.libro.libro_id,
            'ejemplar_id': self.ejemplar_id,
            'CodBarras': self.cod_barras,
            'Subdivision1': self.subdivision1,
            'Subdivision2': self.subdivision2,
            'NoIngreso': self.no_ingreso,
            'FechaIngreso': self.fecha_ingreso,
            'Ubicacion': self.ubicacion,
            'ViasAdq': self.vias_adq,
            'Procedencia': self.procedencia,
            'Precio': self.precio if self.precio is not None else None
        }


def fromJson(json_data):
    libro_id = json_data.get('libro_id')
    # cod_barras = json_data.get('cod_barras')
    subdivision1 = json_data.get('subdivision1')
    subdivision2 = json_data.get('subdivision2')
    no_ingreso = json_data.get('no_ingreso')
    fecha_ingreso = datetime.strptime(
        json_data.get('fecha_ingreso'), '%Y-%m-%d').date()
    ubicacion = json_data.get('ubicacion')
    vias_adq = json_data.get('vias_adq')
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
        vias_adq=vias_adq,
        procedencia=procedencia,
        precio=precio,
    )
    return ejemplar
