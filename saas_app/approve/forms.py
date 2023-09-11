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
            "date_info_requested",
            "info_requested",
            "comments",
            "submitted_by",
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
            "date_info_requested": _("Date Info Requested"),
            "info_requested": _("Info Requested"),
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
            Field(
                "currency",
                disabled=True,
                style="height: auto; color:black; background-color:#e9ecef; opacity:1;font-weight: inherit;font-color: inherit;",
            ),
            Field(
                "frequency",
                disabled=True,
                style="height: auto; color:black; background-color:#e9ecef; opacity:1;font-weight: inherit;font-color: inherit;",
            ),
            Field("units", disabled=True),
            Field("level_of_subscription", disabled=True),
            Field("duration", disabled=True),
            Field("number_of_users", disabled=True),
            Field("names_of_users", disabled=True),
            Field("account_administrator", disabled=True),
            Field("backup_administrator", disabled=True),
            Field(
                "certification",
                disabled=True,
                style="color:black; height:auto; background-color:#e9ecef; opacity:1;font-weight: inherit;font-color: inherit;",
            ),
            Field(
                "google_sign_in",
                disabled=True,
                style="color:black; height:auto; background-color:#e9ecef; opacity:1;font-weight: inherit;font-color: inherit;",
            ),
            Field(
                "manager",
                disabled=True,
                style="color:black; height:auto; background-color:#e9ecef; opacity:1;font-weight: inherit;font-color: inherit;",
            ),
            Field(
                "fund_center",
                disabled=True,
                style="height: auto; color:black; background-color:#e9ecef; opacity:1;font-weight: inherit;font-color: inherit;",
            ),
            Field("comments", disabled=True, rows="5"),
            Field("info_requested", type="hidden"),
            Field("date_info_requested", type="hidden"),
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
        # unhide the date requested and information requested if there is data associated with those fields.
        if self.instance.date_info_requested is not None:
            self.helper["date_info_requested"].update_attributes(
                type="text", readonly=True
            )
        if self.instance.info_requested is not None:
            self.helper["info_requested"].update_attributes(type="text", readonly=True)


class ViewManagerOldRequestForm(ModelForm):
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
            "submitted_by",
            "status",
            "date_manager_reviewed",
            "manager_approved",
            "manager_denied",
            "info_requested",
            "date_info_requested",
        ]
        labels = {
            "name": _("Name of Saas"),
            "status": _("Current status"),
            "currency": _("Currency"),
            "frequency": _("Frequency"),
            "units": _("Units"),
            "duration": _("Duration"),
            "fund_center": _("Fund Center"),
            "certification": _(
                "Does the application have a SOC 2 Type II or ISO 27001 certification? (Hint: this can easily be googled)"
            ),
            "google_sign_in": _("Does the application support 'Sign in with Google'?"),
            "date_manager_reviewed": _("Date manager reviewed the request"),
            "manager_approved": _("Manager approved the request"),
            "manager_denied": _("Manager denied the request"),
            "comments": _("Comments"),
            "date_info_requested": _("Date Info Requested"),
            "info_requested": _("Info Requested"),
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
            Field(
                "currency",
                disabled=True,
                style="height: auto; color:black; background-color:#e9ecef; opacity:1;font-weight: inherit;font-color: inherit;",
            ),
            Field(
                "frequency",
                disabled=True,
                style="height: auto; color:black; background-color:#e9ecef; opacity:1;font-weight: inherit;font-color: inherit;",
            ),
            Field("units", disabled=True),
            Field("level_of_subscription", disabled=True),
            Field("duration", disabled=True),
            Field("number_of_users", disabled=True),
            Field("names_of_users", disabled=True),
            Field("account_administrator", disabled=True),
            Field("backup_administrator", disabled=True),
            Field(
                "certification",
                disabled=True,
                style="color:black; height:auto; background-color:#e9ecef; opacity:1;font-weight: inherit;font-color: inherit;",
            ),
            Field(
                "google_sign_in",
                disabled=True,
                style="color:black; height:auto; background-color:#e9ecef; opacity:1;font-weight: inherit;font-color: inherit;",
            ),
            Field(
                "manager",
                disabled=True,
                style="color:black; height:auto; background-color:#e9ecef; opacity:1;font-weight: inherit;font-color: inherit;",
            ),
            Field(
                "fund_center",
                disabled=True,
                style="height: auto; color:black; background-color:#e9ecef; opacity:1;font-weight: inherit;font-color: inherit;",
            ),
            Field("comments", disabled=True, rows="5"),
            Field(
                "submitted_by",
                disabled=True,
                style="color:black; height:auto; background-color:#e9ecef; opacity:1; font-weight: inherit; font-color: inherit;",
            ),
            Field("status", disabled=True),
            Field("date_manager_reviewed", disabled=True),
            Field("manager_approved", disabled=True),
            Field("manager_denied", disabled=True),
            Field("info_requested", type="hidden"),
            Field("date_info_requested", type="hidden"),
            Button(
                "cancel",
                _("Cancel"),
                css_id="submit",
                css_class="btn btn-primary",
                onclick="history.back()",
            ),
        )
        # unhide the date requested and information requested if there is data associated with those fields.
        if self.instance.date_info_requested is not None:
            self.helper["date_info_requested"].update_attributes(
                type="text", readonly=True
            )
        if self.instance.info_requested is not None:
            self.helper["info_requested"].update_attributes(type="text", readonly=True)


class ViewS32ApproverOldRequestForm(ModelForm):
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
            "submitted_by",
            "status",
            "date_manager_reviewed",
            "manager_approved",
            "manager_denied",
            "info_requested",
            "date_info_requested",
            "date_sent_to_s_32_approver",
            "s_32_review_date",
            "s_32_approved",
        ]
        labels = {
            "name": _("Name of Saas"),
            "status": _("Current status"),
            "currency": _("Currency"),
            "frequency": _("Frequency"),
            "units": _("Units"),
            "duration": _("Duration"),
            "fund_center": _("Fund Center"),
            "certification": _(
                "Does the application have a SOC 2 Type II or ISO 27001 certification? (Hint: this can easily be googled)"
            ),
            "google_sign_in": _("Does the application support 'Sign in with Google'?"),
            "date_manager_reviewed": _("Date manager reviewed the request"),
            "manager_approved": _("Manager approved the request"),
            "manager_denied": _("Manager denied the request"),
            "date_sent_to_s_32_approver": _("Date sent to S32 approver"),
            "s_32_review_date": _("Date S32 approver reviewed the request"),
            "s_32_approved": _("S32 approver approved the request"),
            "comments": _("Comments"),
            "date_info_requested": _("Date Info Requested"),
            "info_requested": _("Info Requested"),
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
            Field(
                "currency",
                disabled=True,
                style="color:black; height:auto; background-color:#e9ecef; opacity:1;font-weight: inherit;font-color: inherit;",
            ),
            Field(
                "frequency",
                disabled=True,
                style="color:black; height:auto; background-color:#e9ecef; opacity:1;font-weight: inherit;font-color: inherit;",
            ),
            Field("units", disabled=True),
            Field("level_of_subscription", disabled=True),
            Field("duration", disabled=True),
            Field("number_of_users", disabled=True),
            Field("names_of_users", disabled=True),
            Field("account_administrator", disabled=True),
            Field("backup_administrator", disabled=True),
            Field(
                "certification",
                disabled=True,
                style="color:black; height:auto; background-color:#e9ecef; opacity:1;font-weight: inherit;font-color: inherit;",
            ),
            Field(
                "google_sign_in",
                disabled=True,
                style="color:black; height:auto; background-color:#e9ecef; opacity:1;font-weight: inherit;font-color: inherit;",
            ),
            Field(
                "manager",
                disabled=True,
                style="color:black; height:auto; background-color:#e9ecef; opacity:1;font-weight: inherit;font-color: inherit;",
            ),
            Field(
                "fund_center",
                disabled=True,
                style="height: auto; color:black; background-color:#e9ecef; opacity:1;font-weight: inherit;font-color: inherit;",
            ),
            Field("comments", disabled=True, rows="5"),
            Field(
                "submitted_by",
                disabled=True,
                style="color:black; height:auto; background-color:#e9ecef; opacity:1; font-weight: inherit; font-color: inherit;",
            ),
            Field("status", disabled=True),
            Field("date_manager_reviewed", disabled=True),
            Field("manager_approved", disabled=True),
            Field("manager_denied", disabled=True),
            Field("info_requested", type="hidden"),
            Field("date_info_requested", type="hidden"),
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
        # unhide the date requested and information requested if there is data associated with those fields.
        if self.instance.date_info_requested is not None:
            self.helper["date_info_requested"].update_attributes(
                type="text", readonly=True
            )
        if self.instance.info_requested is not None:
            self.helper["info_requested"].update_attributes(type="text", readonly=True)
