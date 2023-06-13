from django.http import HttpResponse



def index(request):
    return HttpResponse('This is Homepage')

def index2(request):
    return HttpResponse('This is Second page')