from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Button, Field
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm
from .models import SaasRequest


# Submit Saas Request Form
class SubmitRequestForm(ModelForm):
    # Form is generated from the database fields.
    class Meta:
        model = SaasRequest
        fields = [
            "name",
            "url",
            "description",
            "cost",
            "currency",
            "frequency",
            "units",
            "level_of_subscription",
            "duration",
            "number_of_users",
            "names_of_users",
            "account_administrator",
            "backup_administrator",
            "certification",
            "google_sign_in",
            "manager",
            "fund_center",
            "comments",
        ]
        labels = {
            "name": _("Name of Saas"),
            "currency": _("Currency"),
            "frequency": _("Frequency"),
            "units": _("Units"),
            "duration": _("Duration"),
            "certification": _(
                "Does the application have a SOC 2 Type II or ISO 27001 certification? (Hint: this can easily be googled)"
            ),
            "google_sign_in": _("Does the application support 'Sign in with Google'?"),
            "fund_center": _("Fund Center"),
            "comments": _("Comments"),
        }
        help_texts = {
            "fund_center": _(
                "If Saas is to be used for all of CDS, select FC 110804. If the Saas is to be used specifically for your BU, please select the appropriate FC."
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "submit_request_form"
        self.helper.form_class = "blueForms"
        self.helper.form_method = "post"
        self.helper.form_action = "submit_saas_form"
        self.helper.add_input(Submit("submit", _("Submit")))
        self.fields["comments"].widget.attrs["rows"] = 5
        self.helper.layout = Layout(
            "name",
            "url",
            "description",
            "cost",
            Field("currency", readonly=True, style="height: auto;"),
            Field("frequency", readonly=True, style="height: auto;"),
            "units",
            "level_of_subscription",
            "duration",
            "number_of_users",
            "names_of_users",
            "account_administrator",
            "backup_administrator",
            "certification",
            "google_sign_in",
            Field(
                "manager",
                readonly=True,
                style="height: auto;",
            ),
            Field("fund_center", style="height: auto;"),
            Field("comments", rows="5"),
        )
        self.helper.add_input(
            Button(
                "cancel",
                _("Cancel"),
                css_id="submit",
                css_class="btn btn-primary",
                onclick="history.back()",
            )
        )


# Submit Saas Request Form
class ViewRequestForm(ModelForm):
    # Form is generated from the database fields.
    class Meta:
        model = SaasRequest
        fields = [
            "name",
            "url",
            "description",
            "cost",
            "currency",
            "frequency",
            "units",
            "level_of_subscription",
            "duration",
            "number_of_users",
            "names_of_users",
            "account_administrator",
            "backup_administrator",
            "certification",
            "google_sign_in",
            "manager",
            "fund_center",
            "comments",
        ]
        labels = {
            "name": _("Name of Saas"),
            "currency": _("Currency"),
            "frequency": _("Frequency"),
            "units": _("Units"),
            "duration": _("Duration"),
            "certification": _(
                "Does the application have a SOC 2 Type II or ISO 27001 certification? (Hint: this can easily be googled)"
            ),
            "google_sign_in": _("Does the application support 'Sign in with Google'?"),
            "fund_center": _("Fund Center"),
            "comments": _("Comments"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "view_request_form"
        self.helper.form_class = "blueForms"
        self.helper.layout = Layout(
            "name",
            "url",
            "description",
            "cost",
            Field("currency", readonly=True, style="height: auto;"),
            Field("frequency", readonly=True, style="height: auto;"),
            "units",
            "level_of_subscription",
            "duration",
            "number_of_users",
            "names_of_users",
            "account_administrator",
            "backup_administrator",
            "certification",
            "google_sign_in",
            Field(
                "manager",
                readonly=True,
                style="height:auto;",
            ),
            Field("fund_center", style="height: auto;"),
            Field("comments", rows="5"),
            Submit("save", _("Save changes")),
            Submit(
                "delete",
                _("Delete"),
                onclick="return confirm(_('Are you sure you want to delete this saas request?'));",
            ),
            Button(
                "cancel",
                _("Cancel"),
                css_id="submit",
                css_class="btn btn-primary",
                onclick="history.back()",
            ),
        )


class ViewPrevRequestForm(ModelForm):
    # Form is generated from the database fields.
    class Meta:
        model = SaasRequest
        fields = [
            "name",
            "url",
            "description",
            "cost",
            "currency",
            "frequency",
            "units",
            "level_of_subscription",
            "duration",
            "number_of_users",
            "names_of_users",
            "account_administrator",
            "backup_administrator",
            "certification",
            "google_sign_in",
            "manager",
            "fund_center",
            "comments",
            "status",
        ]
        labels = {
            "name": _("Name of Saas"),
            "status": _("Current status"),
            "currency": _("Currency"),
            "frequency": _("Frequency"),
            "units": _("Units"),
            "duration": _("Duration"),
            "certification": _(
                "Does the application have a SOC 2 Type II or ISO 27001 certification? (Hint: this can easily be googled)"
            ),
            "google_sign_in": _("Does the application support 'Sign in with Google'?"),
            "fund_center": _("Fund Center"),
            "comments": _("Comments"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "view_request_form"
        self.helper.form_class = "blueForms"
        self.helper.layout = Layout(
            Field("name", readonly=True),
            Field("url", readonly=True),
            Field("description", readonly=True),
            Field("cost", readonly=True),
            Field(
                "currency",
                readonly=True,
                style="color:black; height:auto; background-color:#e9ecef; opacity:1;font-weight: inherit;font-color: inherit;",
            ),
            Field(
                "frequency",
                readonly=True,
                style="color:black; height:auto; background-color:#e9ecef; opacity:1;font-weight: inherit;font-color: inherit;",
            ),
            Field("units", readonly=True),
            Field("level_of_subscription", readonly=True),
            Field("duration", readonly=True),
            Field("number_of_users", readonly=True),
            Field("names_of_users", readonly=True),
            Field("account_administrator", readonly=True),
            Field("backup_administrator", readonly=True),
            Field("certification", readonly=True),
            Field("google_sign_in", readonly=True),
            Field(
                "manager",
                readonly=True,
                style="color:black; height:auto; background-color:#e9ecef; opacity:1;font-weight: inherit;font-color: inherit;",
            ),
            Field(
                "fund_center",
                readonly=True,
                style="color:black; height:auto; background-color:#e9ecef; opacity:1;font-weight: inherit;font-color: inherit;",
            ),
            Field("comments", readonly=True, rows="5"),
            Field("status", readonly=True),
            Button(
                "cancel",
                _("Cancel"),
                css_id="submit",
                css_class="btn btn-primary",
                onclick="history.back()",
            ),
        )
