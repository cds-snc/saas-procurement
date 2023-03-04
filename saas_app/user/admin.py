from django.contrib import admin
from .models import Roles, Users


# Register the role and user models to the admin page so that they can be viewed and edited.
@admin.register(Roles)
class RolesAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    list_filter = ("name", "description")
    search_fields = ("name", "description")
    ordering = ("name", "description")


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "first_name",
        "last_name",
        "get_roles",
        "title",
        "business_unit",
    )
    list_filter = (
        "user",
        "first_name",
        "last_name",
        "user_roles",
        "title",
        "business_unit",
    )
    search_fields = (
        "user",
        "first_name",
        "last_name",
        "user_roles",
        "title",
        "business_unit",
    )
    ordering = (
        "user",
        "first_name",
        "last_name",
        "user_roles",
        "title",
        "business_unit",
    )

    # return the roles of the user as a string
    def get_roles(self, obj):
        return ", ".join([p.name for p in obj.user_roles.all()])
