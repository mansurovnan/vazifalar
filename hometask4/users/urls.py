from django.urls import path
from .views import get_best_users, get_users

urlpatterns = [

    path('cars_name', get_best_users),
    path('top_cars', get_users)

]