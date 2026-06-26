from django.http import HttpResponse


def test(request):
    return HttpResponse('sen uddalading')

def home(request):
    return HttpResponse('ma sha alloh sen yana uddalading')