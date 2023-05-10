from django.urls import path
from . import views

app_name = "intenral_ops"

urlpatterns = [
    path("view/", views.view_all_requests, name="view_all_requests"),
    path("view_prev/", views.view_all_prev_requests, name="view_all_prev_requests"),
    path("view/<int:pk>/", views.view_request, name="view_request"),
    path("view_prev/<int:pk>/", views.view_request, name="view_request"),
    path("view/<int:pk>/send_mail", views.send_mail, name="send_mail"),
    path("view/<int:pk>/purchase", views.purchase, name="purchase"),
]
