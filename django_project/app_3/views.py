from django import forms
from django.shortcuts import render


tasks = ["foo", "bar", "baz"]


class NewTaskForm(forms.Form):
    tasks = forms.CharField(label="New Task")


def index(request):
    return render(request, "app_3/index.html", {
        "tasks": tasks
    })


def add(request):
    return render(request, "app_3/add.html", {
        "form": NewTaskForm()
    })


