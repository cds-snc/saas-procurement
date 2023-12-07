from crispy_forms.helper import FormHelper
from django.utils.translation import gettext_lazy as _
from .models import TrainingRequest, Course, Users
from django.forms import ModelForm, TextInput


# Create teh form for hte User information
class UserForm(ModelForm):
    class Meta:
        model = Users
        fields = [
            "first_name",
            "last_name",
            "title",
            "dept_email",
            "telephone",
            "sector",
            "group",
            "level",
            "city",
        ]
        labels = {
            "title": _("Position Title"),
            "dept_email": _("E-Mail"),
        }
        help_texts = {
            "telephone": _(
                "Valid phone numbers of the form +1 + area code + phone number (e.g. +12125552368)."
            )
        }

    # Constructor to initialize the form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "user_form"
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.fields["title"].required = True
        self.fields["dept_email"].required = True
        self.fields["telephone"].required = True
        self.fields["sector"].required = True
        self.fields["group"].required = True
        self.fields["level"].required = True
        self.fields["city"].required = True


# Create the form for the Course that the user wants to take
class CourseForm(ModelForm):
    class Meta:
        model = Course
        widgets = {
            "start_date": TextInput(attrs={"class": "datepicker", "type": "date"}),
        }
        fields = [
            "course_title",
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
            "course_title": _("Name of Course"),
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
        self.fields["currency"].required = True


# Training Request Form
class TrainingForm(ModelForm):
    # Form is generated from the database fields.
    class Meta:
        model = TrainingRequest
        fields = [
            "fund_center",
            "s32_approved_by",
            "travel_living_costs",
            "manager",
            "comments",
        ]
        labels = {
            "s32_approved_by": _("Fund Center Manager"),
            "manager": _("Your Manager"),
        }

    # Initial constructor to initialize the form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "training_request_form"
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.fields["fund_center"].required = True
        self.fields["s32_approved_by"].required = True
