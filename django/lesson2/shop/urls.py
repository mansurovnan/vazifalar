from django.contrib import admin
from django.urls import path
from .test import test, home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', test),
    path('index', home)
]
