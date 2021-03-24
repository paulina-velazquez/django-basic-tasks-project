from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),  # Added new path. Takes a string as the "name"
    path("paulina", views.paulina, name="paulina")
]
