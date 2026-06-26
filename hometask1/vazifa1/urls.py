from django.contrib import admin
from django.urls import path
from names.views import get_users, get_best_users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('names', get_users),
    path('best_users', get_best_users)
    
]


