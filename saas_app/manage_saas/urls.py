from django.urls import path
from . import views

app_name = "manage_saas"

urlpatterns = [
    path("view_logs/", views.view_logs, name="view_logs"),
]
