from django.db import models

# Create your models here.


class Materia(models.Model):
    materia_id = models.AutoField(primary_key=True)
    name = models.TextField(null=True)
    
    class Meta:
        db_table = "materia"

    def to_dict(self):
        return {
            'materia_id': self.materia_id,
            'name': self.name
        }


def parseParams(request):
    name = request.GET.get('name')
    return {
        "name": name
    }
