from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.conf.urls.i18n import i18n_patterns
from . import views


urlpatterns = i18n_patterns(
    path("admin/", admin.site.urls),
    path("", views.init, name="home"),
    path("role", views.switch_role, name="switch_role"),
    path("accounts/", include("allauth.urls")),
    path("logout", LogoutView.as_view()),
    path("submit_request/", include("submit_request.urls")),
    path("approve/", include("approve.urls"), name="approve"),
    path("internal_ops/", include("internal_ops.urls"), name="internal_ops"),
    path("search/", views.search, name="search"),
    path("search/<int:pk>/", views.view_request, name="view_request"),
    path("administration/", include("administration.urls"), name="administration"),
    path("manage_saas/", include("manage_saas.urls"), name="manage_saas"),
    path("i18n/", include("django.conf.urls.i18n")),
)
