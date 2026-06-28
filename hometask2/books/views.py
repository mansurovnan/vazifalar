from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def get_books(request):
    return HttpResponse('men ufq ikki eshik orasi')

def get_top_book(request):
    return HttpResponse('Binafsha shulasi')
