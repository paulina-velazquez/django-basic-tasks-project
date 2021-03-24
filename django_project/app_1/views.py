from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")


# ******* Added a new view called Paulina
def paulina(request):
    return HttpResponse("Hello, Paulina!")
