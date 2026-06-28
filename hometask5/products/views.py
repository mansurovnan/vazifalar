from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def get_names(request):
    return HttpResponse('malika, odina')
def get_best_names(request):
    return HttpResponse('umar')