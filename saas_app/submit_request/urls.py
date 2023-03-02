from django.urls import path
from . import views

urlpatterns = [
    path("", views.process_requets, name="submit_request"),
]
