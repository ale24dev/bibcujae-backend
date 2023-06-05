from rest_framework import serializers
from .models import Ejemplar


class EjemplarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejemplar
        fields = '__all__'
