from django.contrib import admin
from .models import FundCenter

# Register the Fund center model with the Admin menu


# Register the SaasRequest model to the admin page so that it can be viewed and edited.
@admin.register(FundCenter)
class FundCenterAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "number",
    )
    list_filter = (
        "name",
        "number",
    )
    search_fields = (
        "name",
        "number",
    )
    ordering = (
        "name",
        "number",
    )
