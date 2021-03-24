from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("paulina", views.paulina, name="paulina")  # **** Added new path to views folder function paulina
]
