import json
from django.db import models
from django.core.serializers import serialize

from book.models import Book
from materia.models import Materia


class MateriaLibros(models.Model):
    materiaLibro_id = models.AutoField(primary_key=True)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    libro = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        db_table = "materiaLibros"

    def to_dict(self):
        materia = json.loads(serialize(
            'json', [Materia.objects.get(materia_id=self.materia.materia_id)]))[0]
        book = json.loads(serialize('json', [Book.objects.get(
            libro_id=self.libro.libro_id)]))[0]

        materia["fields"]["materia_id"] = materia["pk"]
        book["fields"]["libro_id"] = book["pk"]

        return {
            'materiaLibro_id': self.materiaLibro_id,
            'materia': materia["fields"],
            'libro': book["fields"],
        }
