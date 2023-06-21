from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Button, Field
from django.forms import ModelForm
from django.utils.translation import get_language, gettext_lazy as _
from django.db import models
from user.models import Users

# get the current language
current_language = get_language()

# View a Saas Request Form
class ViewUserForm(ModelForm):
    # Form is generated from the database fields.
    class Meta:
        model = Users 
        fields = [
            "first_name",
            "last_name",
            "user_roles",
            "title",
            "business_unit",
        ]
        labels = {
            "first_name": _("First Name"),
            "last_name": _("Last Name"),
            "user_roles": _("User Roles"),
            "title": _("Title"),
            "business_unit": _("Business Unit"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "view_user_form"
        self.helper.form_class = "blueForms"
        self.helper.layout = Layout(
            "first_name",
            "last_name",
            Field.checkboxes("user_roles"),
            Field("user_roles", css_class="select2"),
            "user_roles",
            "title",
            "business_unit",
            Button(
                "update_roles",
                _("Update roles"),
                css_id="submit",
                css_class="btn btn-primary",
                data_toggle="modal",
                data_target="#update_roles_modal",
                data_dismiss="modal",
            ),
            Submit(
                "save",
                _("Save"),
            ),
            Button(
                "cancel",
                _("Cancel"),
                css_id="submit",
                css_class="btn btn-primary",
                onclick="window.location.href='/"
                + current_language
                + "/administration/view'",
            ),
        )