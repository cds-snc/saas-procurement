from crispy_forms.helper import FormHelper
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm
from .models import TrainingRequest, Course


# Create the form for the Course that the user wants to take
class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = [
            "title",
            "description",
            "provider",
            "language",
            "start_date",
            "duration",
            "location",
            "cost",
            "currency",
        ]
        labels = {
            "title": _("Name of Course"),
            "description": _("Description of Course"),
            "provider": _("Course Provider"),
            "language": _("Language of Course"),
            "units": _("Units"),
            "duration": _("Duration"),
            "location": _("Course Location"),
        }

    # Constructor to initialize the form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "course_form"
        self.helper.form_tag = False
        self.helper.disable_csrf = True


# Training Request Form
class TrainingForm(ModelForm):
    # Form is generated from the database fields.
    class Meta:
        model = TrainingRequest
        fields = [
            "fund_center",
            "travel_living_costs",
            "manager",
            "comments",
        ]
        labels = {
            "manager": _("Your Manager"),
        }

    # Initial constructor to initialize the form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "training_request_form"
        self.helper.form_tag = False
        self.helper.disable_csrf = True
