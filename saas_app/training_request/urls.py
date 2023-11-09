from django.urls import path
from . import views

app_name = "training_request"

urlpatterns = [
    path("", views.process_requests, name="training_request"),
    path("view/", views.view_all_requests, name="view_all_requests"),
    path("view/<int:pk>/", views.view_request, name="view_request"),
]
