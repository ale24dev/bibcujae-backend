from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import RegisterSerializer, CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data.get('password')
            username = serializer.validated_data.get('username')
            email = serializer.validated_data.get('email')

            # Crear el usuario utilizando el modelo de usuario de Django
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            user.save()

            # Crear y retornar el token de autenticación
            token = RefreshToken.for_user(user)
            response_data = {
                'refresh': str(token),
                'access': str(token.access_token)
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)