from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")


def paulina(request):
    return HttpResponse("Hello, Paulina!")


# **Added a new function called "greet"
def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")
