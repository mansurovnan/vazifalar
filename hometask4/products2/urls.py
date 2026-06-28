from django.urls import path
from .views import get_best_products, get_products

urlpatterns = [

    path('cars_name', get_products),
    path('top_cars', get_best_products)

]

