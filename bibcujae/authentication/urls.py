from django.urls import path
from .views import CustomTokenObtainPairView, RegisterView

urlpatterns = [
    path('api/auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtener'),
    path('api/auth/register/', RegisterView.as_view(), name='register'),
]