from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def get_users_name(request):
    return HttpResponse('Umid, Islom, Ibrohim')

def get_top_user_name(request):
    return HttpResponse('Muhammad, Ismoil')
