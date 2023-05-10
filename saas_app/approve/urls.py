from django.urls import path
from . import views


app_name = "approve"

urlpatterns = [
    path("view/", views.view_all_requests, name="view_all_requests"),
    path("view_prev/", views.view_all_prev_requests, name="view_all_prev_requests"),
    path("view/<int:pk>/", views.view_request, name="view_request"),
    path("view_prev/<int:pk>/", views.view_request, name="view_request"),
    path(
        "view_s32/",
        views.view_all_requests_s32_approver,
        name="view_all_requests_s32_approver",
    ),
    path(
        "view_s32_prev/",
        views.view_all_prev_requests_s32_approver,
        name="view_all_prev_requests_s32_approver",
    ),
    path(
        "view_s32/<int:pk>/",
        views.view_request_s32_approver,
        name="view_request_s32_approver",
    ),
    path(
        "view_s32_prev/<int:pk>/",
        views.view_request_s32_approver,
        name="view_request_s32_approver",
    ),
]
