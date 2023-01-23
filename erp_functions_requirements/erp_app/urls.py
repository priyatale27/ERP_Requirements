from django.urls import path
from .views import *


urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('user_login/', LoginAPI.as_view(), name='user_login'),
]