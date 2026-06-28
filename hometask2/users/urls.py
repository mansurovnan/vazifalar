from django.urls import path
from .views import get_users_name, get_top_user_name

urlpatterns = [
    path('users_name', get_users_name),
    path('top_users/', get_top_user_name)
]
