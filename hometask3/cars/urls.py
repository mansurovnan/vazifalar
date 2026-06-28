from django.urls import path
from .views import get_cars, top_cars

urlpatterns = [
    path('', get_cars),
    path('top_cars', top_cars)

]