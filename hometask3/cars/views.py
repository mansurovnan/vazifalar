from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def get_cars(request):
    return HttpResponse('cobalt, spark jentra')
def top_cars(request):
    return HttpResponse("jentra legenda))")