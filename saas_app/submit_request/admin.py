from django.contrib import admin
from .models import SaasRequest

# Register the SaasRequest model to the admin page so that it can be viewed and edited.
@admin.register(SaasRequest)
class SaasRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'description', 'cost', 'level_of_subscription', 'number_of_users', 'names_of_users', 'account_administrator', 'backup_administrator', 'approver')
    list_filter = ('name', 'url', 'description', 'cost', 'level_of_subscription', 'number_of_users', 'names_of_users', 'account_administrator', 'backup_administrator', 'approver')
    search_fields = ('name', 'url', 'description', 'cost', 'level_of_subscription', 'number_of_users', 'names_of_users', 'account_administrator', 'backup_administrator', 'approver')
    ordering = ('name', 'url', 'description', 'cost', 'level_of_subscription', 'number_of_users', 'names_of_users', 'account_administrator', 'backup_administrator', 'approver')
