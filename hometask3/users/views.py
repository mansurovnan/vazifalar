from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def get_cars_user(request):
    return HttpResponse('Ibrohimning mashinasi')

def get_top_user(request):
    return HttpResponse('Ahmads cars is the best')
