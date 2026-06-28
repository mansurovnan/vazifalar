from django.urls import path
from .views import get_cars_user, get_top_user

urlpatterns = [
    path('', get_top_user),
    path('cars_users', get_cars_user )

]