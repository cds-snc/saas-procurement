from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "training_request"

urlpatterns = [
    path("", views.process_requests, name="training_request"),
    path("view/", views.view_all_requests, name="view_all_requests"),
    path("view/<int:pk>/", views.view_request, name="view_request"),
    path("download/", views.download, name="download"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
