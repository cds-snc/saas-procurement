from django.urls import path
from . import views

app_name = "administration"

urlpatterns = [
    path("view/", views.view_users, name="view_users"),
    path("view/<int:pk>/", views.view_user, name="view_user"),
    #path("view_logs/", views.view_logs, name="view_logs"),
]
