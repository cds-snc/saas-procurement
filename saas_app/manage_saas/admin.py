from django.contrib import admin
from .models import GoogleWorkspaceAppsLogin


# Register the SaasRequest model to the admin page so that it can be viewed and edited.
@admin.register(GoogleWorkspaceAppsLogin)
class GoogleWorkspaceAppsLoginAdmin(admin.ModelAdmin):
    list_display = (
        "time_generated",
        "source_system",
        "kind",
        "application_name",
        "user_email",
        "user_ip_address",
        "event_name",
        "client_id",
        "application_name_id",
        "client_type",
        "scope_data",
        "scope",
        "geolocation_country",
        "geolocation_city",
        "type",
    )
    list_filter = (
        "time_generated",
        "source_system",
        "kind",
        "application_name",
        "user_email",
        "user_ip_address",
        "event_name",
        "client_id",
        "application_name_id",
        "client_type",
        "scope_data",
        "scope",
        "geolocation_country",
        "geolocation_city",
        "type",
    )
    search_fields = (
        "time_generated",
        "source_system",
        "kind",
        "application_name",
        "user_email",
        "user_ip_address",
        "event_name",
        "client_id",
        "application_name_id",
        "client_type",
        "scope_data",
        "scope",
        "geolocation_country",
        "geolocation_city",
        "type",
    )
    ordering = (
        "time_generated",
        "source_system",
        "kind",
        "application_name",
        "user_email",
        "user_ip_address",
        "event_name",
        "client_id",
        "application_name_id",
        "client_type",
        "scope_data",
        "scope",
        "geolocation_country",
        "geolocation_city",
        "type",
    )
