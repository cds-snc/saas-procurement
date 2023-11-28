from django.contrib import admin
from .models import TrainingRequest, Course


# Set up the appropriate display fields, list fields and search fields for the admin page for the Course model
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "course_title",
        "description",
        "provider",
        "language",
        "start_date",
        "duration",
        "location",
        "cost",
        "currency",
    )
    list_filter = (
        "course_title",
        "description",
        "provider",
        "language",
        "start_date",
        "duration",
        "location",
        "cost",
        "currency",
    )
    search_fields = (
        "course_title",
        "description",
        "provider",
        "language",
        "start_date",
        "duration",
        "location",
        "cost",
        "currency",
    )


# Set up the appropriate display fields, list fields and search fields for the admin page for the Training Request model
@admin.register(TrainingRequest)
class TrainingRequestAdmin(admin.ModelAdmin):
    list_display = (
        "course",
        "fund_center",
        "travel_living_costs",
        "submitted_by",
        "status",
        "manager",
        "date_submitted",
        "date_manager_reviewed",
        "s32_approved_by",
        "date_s32_reviewed",
        "comments",
        "pdf_form",
    )
    list_filter = (
        "course",
        "fund_center",
        "travel_living_costs",
        "submitted_by",
        "status",
        "manager",
        "date_submitted",
        "date_manager_reviewed",
        "s32_approved_by",
        "date_s32_reviewed",
        "comments",
        "pdf_form"
    )
    search_fields = (
        "course",
        "fund_center",
        "travel_living_costs",
        "submitted_by",
        "status",
        "manager",
        "date_submitted",
        "date_manager_reviewed",
        "s32_approved_by",
        "date_s32_reviewed",
        "comments",
        "pdf_form"
    )
