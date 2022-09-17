from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.
### functions


def helloworld(request):
    return HttpResponse("Hello world from django ")  # plain text


def my_info(request): # http request
    l = ["noha", "Deviops"]
    return HttpResponse(l)



def homepage(request):
    return render(request, "home.html")