from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def get_products(request):
    return HttpResponse("olma anor o'rik")
def get_best_products(request):
    return HttpResponse('the best product is only APPLE')
