from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Button, Field
from django.forms import ModelForm
from submit_request.models import SaasRequest
from django.utils.translation import gettext_lazy as _


# View a Saas Request Form
class ViewRequestForm(ModelForm):
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
            "submitted_by",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "view_request_form"
        self.helper.form_class = "blueForms"
        self.helper.layout = Layout(
            Field("name", disabled=True),
            Field("url", disabled=True),
            Field("description", disabled=True),
            Field("cost", disabled=True),
            Field("level_of_subscription", disabled=True),
            Field("number_of_users", disabled=True),
            Field("names_of_users", disabled=True),
            Field("account_administrator", disabled=True),
            Field("backup_administrator", disabled=True),
            Field(
                "manager",
                disabled=True,
                style="color:black; height:auto; background-color:#e9ecef; opacity:1;font-weight: inherit;font-color: inherit;",
            ),
            Field(
                "submitted_by",
                disabled=True,
                style="color:black; height:auto; background-color:#e9ecef; opacity:1; font-weight: inherit; font-color: inherit;",
            ),
            Submit("approve", _("Approve")),
            Submit(
                "deny",
                _("Deny"),
                onclick="return confirm(_('Are you sure you want to deny this saas request?'));",
            ),
            Button(
                "cancel",
                _("Cancel"),
                css_id="submit",
                css_class="btn btn-primary",
                onclick="history.back()",
            ),
        )


class ViewManagerOldRequestForm(ModelForm):
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
            "submitted_by",
            "status",
            "date_manager_reviewed",
            "manager_approved",
            "manager_denied",
        ]
        labels = {
            "status": _("Current status"),
            "date_manager_reviewed": _("Date manager reviewed the request"),
            "manager_approved": _("Manager approved the request"),
            "manager_denied": _("Manager denied the request"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "view_request_form"
        self.helper.form_class = "blueForms"
        self.helper.layout = Layout(
            Field("name", disabled=True),
            Field("url", disabled=True),
            Field("description", disabled=True),
            Field("cost", disabled=True),
            Field("level_of_subscription", disabled=True),
            Field("number_of_users", disabled=True),
            Field("names_of_users", disabled=True),
            Field("account_administrator", disabled=True),
            Field("backup_administrator", disabled=True),
            Field(
                "manager",
                disabled=True,
                style="color:black; height:auto; background-color:#e9ecef; opacity:1;font-weight: inherit;font-color: inherit;",
            ),
            Field(
                "submitted_by",
                disabled=True,
                style="color:black; height:auto; background-color:#e9ecef; opacity:1; font-weight: inherit; font-color: inherit;",
            ),
            Field("status", disabled=True),
            Field("date_manager_reviewed", disabled=True),
            Field("manager_approved", disabled=True),
            Field("manager_denied", disabled=True),
            Button(
                "cancel",
                _("Cancel"),
                css_id="submit",
                css_class="btn btn-primary",
                onclick="history.back()",
            ),
        )


class ViewS32ApproverOldRequestForm(ModelForm):
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
            "submitted_by",
            "status",
            "date_manager_reviewed",
            "manager_approved",
            "manager_denied",
            "date_sent_to_s_32_approver",
            "s_32_review_date",
            "s_32_approved",
        ]
        labels = {
            "status": _("Current status"),
            "date_manager_reviewed": _("Date manager reviewed the request"),
            "manager_approved": _("Manager approved the request"),
            "manager_denied": _("Manager denied the request"),
            "date_sent_to_s_32_approver": _("Date sent to S32 approver"),
            "s_32_review_date": _("Date S32 approver reviewed the request"),
            "s_32_approved": _("S32 approver approved the request"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "view_request_form"
        self.helper.form_class = "blueForms"
        self.helper.layout = Layout(
            Field("name", disabled=True),
            Field("url", disabled=True),
            Field("description", disabled=True),
            Field("cost", disabled=True),
            Field("level_of_subscription", disabled=True),
            Field("number_of_users", disabled=True),
            Field("names_of_users", disabled=True),
            Field("account_administrator", disabled=True),
            Field("backup_administrator", disabled=True),
            Field(
                "manager",
                disabled=True,
                style="color:black; height:auto; background-color:#e9ecef; opacity:1;font-weight: inherit;font-color: inherit;",
            ),
            Field(
                "submitted_by",
                disabled=True,
                style="color:black; height:auto; background-color:#e9ecef; opacity:1; font-weight: inherit; font-color: inherit;",
            ),
            Field("status", disabled=True),
            Field("date_manager_reviewed", disabled=True),
            Field("manager_approved", disabled=True),
            Field("manager_denied", disabled=True),
            Field("date_sent_to_s_32_approver", disabled=True),
            Field("s_32_review_date", disabled=True),
            Field("s_32_approved", disabled=True),
            Button(
                "cancel",
                _("Cancel"),
                css_id="submit",
                css_class="btn btn-primary",
                onclick="history.back()",
            ),
        )
