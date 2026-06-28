from django.urls import path
from .views import get_names, get_best_names
 
urlpatterns = [
    path('names', get_names),
    path('best_names', get_best_names),


]