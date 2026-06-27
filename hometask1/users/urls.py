from django.urls import path
from .views import signing, signup

urlpatterns = [
  path('login', signing),
    path('regis',  signup)
]