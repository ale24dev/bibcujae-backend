import json

from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView


from .utils import to_dict
from .serializers import RegisterSerializer, CustomTokenObtainPairSerializer


# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer


# class RegisterView(APIView):

def post(self, request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        password = serializer.validated_data.get('password')
        username = serializer.validated_data.get('username')

        # Crear el usuario utilizando el modelo de usuario de Django
        user = User.objects.create_user(
            username=username,
            password=password,
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


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        username = data.get('username')
        password = data.get('password')

        if username is None or password is None:
            return Response({'error': 'Por favor, proporcione ambos username y password'},
                            status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if not user:
            return Response({'error': 'Credenciales inválidas'},
                            status=status.HTTP_404_NOT_FOUND)

        token = RefreshToken.for_user(user)
        response_data = {
            'user_id': user.pk,
            'refresh': str(token),
            'access': str(token.access_token)
        }
    return Response(response_data)

@api_view(['GET'])
@permission_classes([AllowAny])
def getAllUsers(request):
    if request.method == 'GET':
        users = User.objects.all()
        users_list = [to_dict(user) for user in users]
        return Response(users_list)
