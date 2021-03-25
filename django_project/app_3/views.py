from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse




class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")


def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "app_3/index.html", {
        "tasks": request.session["tasks"]
    })


def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            return HttpResponseRedirect(reverse("app_3:index"))
        else:
            return render(request, "app_3/add.html", {
                "form": form
            })

    return render(request, "app_3/add.html", {
        "form": NewTaskForm()
    })


