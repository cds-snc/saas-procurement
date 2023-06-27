from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Button
from crispy_forms.bootstrap import InlineCheckboxes
import django.forms as forms
from django.utils.translation import get_language, gettext_lazy as _
from user.models import Users, Roles

# get the current language
current_language = get_language()


# View a Saas Request Form
class ViewUserForm(forms.ModelForm):
    # user roles multiple choice field
    user_roles = forms.ModelMultipleChoiceField(
        queryset=Roles.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label=_("User Roles:"),
        required=False,
    )

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
            InlineCheckboxes(_("user_roles")),
            "title",
            "business_unit",
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
