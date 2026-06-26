from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def get_users(request):
    return HttpResponse('malika, odina')
def get_best_users(request):
    return HttpResponse('umar')