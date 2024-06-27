from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path("", views.Index, name="index"),
    path("success/", views.Success, name="success"),
]
