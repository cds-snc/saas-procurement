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
        "approver",
        "submitted_by",
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
        "approver",
        "submitted_by",
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
        "approver",
        "submitted_by",
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
        "approver",
        "submitted_by",
    )
