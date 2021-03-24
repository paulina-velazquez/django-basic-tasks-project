from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "app_1/index.html")


def paulina(request):
    return HttpResponse("Hello, Paulina!")


def greet(request, name):
    return render(request, "app_1/greet.html", {
        "name": name.capitalize()  # context: Information to provide to the templates.
    })