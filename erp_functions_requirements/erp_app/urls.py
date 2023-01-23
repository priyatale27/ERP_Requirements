from django.urls import path
from .views import *


urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('user_login/', LoginAPI.as_view(), name='user_login'),
    path('user_location/', UserDetailAPIView.as_view(), name='user_location'),
    path('ug_login/', LoginUnderGroupAPI.as_view(), name='ug_login'),

]