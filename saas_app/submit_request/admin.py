from django.contrib import admin
from .models import SaasRequest, Currency, Frequency


# Register the currency model to the admin page so that it can be viewed and edited.
@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("currency",)
    list_filter = ("currency",)
    search_fields = ("currency",)
    ordering = ("currency",)


# Register the frequency model to the admin page so that it can be viewed and edited.
@admin.register(Frequency)
class FrequencyAdmin(admin.ModelAdmin):
    list_display = ("frequency",)
    list_filter = ("frequency",)
    search_fields = ("frequency",)
    ordering = ("frequency",)


# Register the SaasRequest model to the admin page so that it can be viewed and edited.
@admin.register(SaasRequest)
class SaasRequestAdmin(admin.ModelAdmin):
    list_display = (
        "id",
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
        "status",
        "manager_approved",
        "approved_by",
        "date_manager_reviewed",
        "manager_denied",
        "s_32_approved",
        "s_32_review_date",
        "date_sent_to_s_32_approver",
        "purchase_date",
        "purchased",
        "date_info_requested",
        "fund_center",
        "purchase_amount",
        "purchase_method",
        "confirmation_number",
        "purchase_notes",
        "certification",
        "google_sign_in",
        
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
        "status",
        "approved_by",
        "date_manager_reviewed",
        "manager_approved",
        "manager_denied",
        "s_32_approved",
        "s_32_review_date",
        "date_sent_to_s_32_approver",
        "purchase_date",
        "purchased",
        "date_info_requested",
        "fund_center",
        "purchase_amount",
        "purchase_method",
        "confirmation_number",
        "purchase_notes",
        "certification",
        "google_sign_in",
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
        "status",
        "manager_approved",
        "approved_by",
        "date_manager_reviewed",
        "manager_denied",
        "s_32_approved",
        "s_32_review_date",
        "date_sent_to_s_32_approver",
        "purchase_date",
        "purchased",
        "date_info_requested",
        "fund_center",
        "purchase_amount",
        "purchase_method",
        "confirmation_number",
        "purchase_notes",
        "certification",
        "google_sign_in"
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
        "status",
        "manager_approved",
        "approved_by",
        "date_manager_reviewed",
        "manager_denied",
        "s_32_approved",
        "s_32_review_date",
        "date_sent_to_s_32_approver",
        "purchase_date",
        "date_info_requested",
        "fund_center",
        "purchase_amount",
        "purchase_method",
        "confirmation_number",
        "purchase_notes",
        "certification",
        "google_sign_in"
    )
