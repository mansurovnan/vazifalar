from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def get_users(request):
    return HttpResponse("ibrohimning olma anor o'rik mevalari bor")
def get_best_users(request):
    return HttpResponse("the best product is only APPLE of ilhom's")
