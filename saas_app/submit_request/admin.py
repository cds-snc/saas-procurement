from django.contrib import admin
from .models import SaasRequest


# Register the SaasRequest model to the admin page so that it can be viewed and edited.
@admin.register(SaasRequest)
class SaasRequestAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "url",
        "description",
        "cost",
        "level_of_subscription",
        "number_of_users",
        "names_of_users",
        "account_administrator",
        "backup_administrator",
        "manager",
        "submitted_by",
        "date_submitted",
        "manager_approved",
        "approved_by",
        "date_manager_reviewed",
        "manager_denied",
    )
    list_filter = (
        "name",
        "url",
        "description",
        "cost",
        "level_of_subscription",
        "number_of_users",
        "names_of_users",
        "account_administrator",
        "backup_administrator",
        "manager",
        "submitted_by",
        "date_submitted",
        "approved_by",
        "date_manager_reviewed",
        "manager_approved",
        "manager_denied",
    )
    search_fields = (
        "name",
        "url",
        "description",
        "cost",
        "level_of_subscription",
        "number_of_users",
        "names_of_users",
        "account_administrator",
        "backup_administrator",
        "manager",
        "submitted_by",
        "date_submitted",
        "manager_approved",
        "approved_by",
        "date_manager_reviewed",
        "manager_denied",
    )
    ordering = (
        "name",
        "url",
        "description",
        "cost",
        "level_of_subscription",
        "number_of_users",
        "names_of_users",
        "account_administrator",
        "backup_administrator",
        "manager",
        "submitted_by",
        "date_submitted",
        "manager_approved",
        "approved_by",
        "date_manager_reviewed",
        "manager_denied",
    )
