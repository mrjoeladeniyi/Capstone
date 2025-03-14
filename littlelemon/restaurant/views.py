from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sayHello(request):
    return HttpResponse('Hello world')

def index(request):
    return render(request, 'index.html', {})