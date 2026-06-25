from django.contrib import admin
from django.urls import path
from .vazifa2 import test, home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', test),
    path('index', home)
]

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
