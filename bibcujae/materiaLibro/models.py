from django.db import models
from materia.models import Materia
from book.models import Book

# Create your models here.
class MateriaLibro(models.Model):
    materiaLibro_id = models.AutoField(primary_key=True)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    libro = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        db_table = "materiaLibro"
    def to_dict(self):
        
        return {
            'materiaLibro_id': self.materia_id,
            'materia': self.name,
            'libro': self.name,
        }


# def parseParams(request):
#     name = request.GET.get('name')
#     return {
#         "name": name
#     }