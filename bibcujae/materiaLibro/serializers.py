from rest_framework import serializers
from .models import MateriaLibro


class MateriaLibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = MateriaLibro
        fields = '__all__'
