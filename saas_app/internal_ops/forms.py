from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Button, Field
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from submit_request.models import SaasRequest


# View a Saas Request Form
class ViewS32RequestForm(ModelForm):
    # Form is generated from the database fields.
    class Meta:
        model = SaasRequest
        fields = [
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
            "date_manager_reviewed",
            "submitted_by",
            "fund_center",
            "approved_by",
        ]
        labels = {
            "name": _("Name"),
            "url": _("URL"),
            "description": _("Description"),
            "cost": _("Cost"),
            "level_of_subscription": _("Level of Subscription"),
            "number_of_users": _("Number of Users"),
            "names_of_users": _("Names of Users"),
            "account_administrator": _("Account Administrator"),
            "backup_administrator": _("Backup Administrator"),
            "manager": _("Manager"),
            "date_manager_reviewed": _("Date Manager Approved the request"),
            "submitted_by": _("Submitted By"),
            "fund_center": _("Fund Center"),
            "approved_by": _("S32 Approver"),
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
            Field("level_of_subscription", readonly=True),
            Field("number_of_users", readonly=True),
            Field("names_of_users", readonly=True),
            Field("account_administrator", readonly=True),
            Field("backup_administrator", readonly=True),
            Field(
                "manager",
                readonly=True,
                style="color:black; background-color:#e9ecef; opacity:1;font-weight: inherit;font-color: inherit;",
            ),
            Field("date_manager_reviewed", readonly=True),
            Field(
                "submitted_by",
                readonly=True,
                style="color:black; background-color:#e9ecef; opacity:1; font-weight: inherit; font-color: inherit;",
            ),
            Field("fund_center"),
            Field("approved_by"),
            Submit(
                "save",
                _("Save"),
                css_class="btn btn-primary btn-lg",
            ),
            Submit("send_for_s32_approval", _("Send for S32 Approval")),
            Button(
                "request_info",
                _("Request Additional Information"),
                css_id="submit",
                css_class="btn btn-primary btn-lg",
                data_toggle="modal",
                data_target="#request_info_modal",
                data_dismiss="modal",
            ),
            Button(
                "purchase",
                _("Record Purchase Information"),
                css_id="submit",
                css_class="btn btn-primary btn-lg",
                data_toggle="modal",
                data_target="#purchase_modal",
                data_dismiss="modal",
            ),
            Button(
                "cancel",
                _("Cancel"),
                css_id="submit",
                css_class="btn btn-primary btn-lg",
                onclick="history.back()",
            ),
        )
