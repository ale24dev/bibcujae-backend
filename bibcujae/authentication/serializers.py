from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['usuario_id'] = self.user.id
        data['usuario_nombre'] = self.user.username
        return data

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128, write_only=True)
    email = serializers.EmailField()

    def validate_username(self, value):
        """
        Verificar si ya existe un usuario con el mismo nombre de usuario
        """
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Ya existe un usuario con este nombre de usuario.')
        return value

    def create(self, validated_data):
        """
        Crear un nuevo usuario
        """
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user