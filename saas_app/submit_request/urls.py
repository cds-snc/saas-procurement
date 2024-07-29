from django.urls import path
from . import views

app_name = "submit_request"

urlpatterns = [
    path("", views.process_requests, name="submit_request"),
    path("thanks/", views.thank_you_view, name="thanks"),
    path("view/", views.view_all_requests, name="view_all_requests"),
    path("view/<int:pk>/", views.view_request, name="view_request"),
]
