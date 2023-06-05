from django.urls import path
# from .views import CustomTokenObtainPairView, RegisterView, login
from .views import login, getAllUsers

urlpatterns = [
    #path('api/auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtener'),
    path('api/auth/login/', login, name='token_obtener'),
    path('api/auth/user/all', getAllUsers, name='get_all_users'),
    # path('api/auth/register/', RegisterView.as_view(), name='register'),
]