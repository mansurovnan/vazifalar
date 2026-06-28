from django.urls import path
from .views import get_books, get_top_book

urlpatterns = [
    path('books', get_books),
    path('top_books/', get_top_book),
]