from rest_framework import serializers
from .models import MateriaLibros


class MateriaLibrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = MateriaLibros
        fields = '__all__'
