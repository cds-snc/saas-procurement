from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Button, Field
from django.forms import ModelForm
from django.utils.translation import get_language, gettext_lazy as _
from submit_request.models import SaasRequest

# get the current language
current_language = get_language()


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
            "currency",
            "frequency",
            "units",
            "level_of_subscription",
            "duration",
            "number_of_users",
            "names_of_users",
            "account_administrator",
            "backup_administrator",
            "manager",
            "comments",
            "date_manager_reviewed",
            "submitted_by",
            "date_info_requested",
            "info_requested",
            "fund_center",
            "approved_by",
        ]
        labels = {
            "name": _("Name of Saas"),
            "url": _("URL"),
            "description": _("Description"),
            "cost": _("Cost"),
            "currency": _("Currency"),
            "frequency": _("Frequency"),
            "units": _("Units"),
            "level_of_subscription": _("Level of Subscription"),
            "duration": _("Duration"),
            "number_of_users": _("Number of Users"),
            "names_of_users": _("Names of Users"),
            "account_administrator": _("Account Administrator"),
            "backup_administrator": _("Backup Administrator"),
            "manager": _("Manager"),
            "comments": _("Comments"),
            "date_manager_reviewed": _("Date Manager reviewed the request"),
            "manager_approved": _("Manager Approved"),
            "manager_denied": _("Manager Denied"),
            "submitted_by": _("Submitted By"),
            "fund_center": _("Fund Center"),
            "approved_by": _("S32 Approver"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "view_request_form"
        self.helper.form_class = "blueForms"
        self.fields["date_info_requested"].label = False
        self.fields["info_requested"].label = False
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
            Field(
                "manager",
                readonly=True,
                style="color:black; height:auto; background-color:#e9ecef; opacity:1;font-weight: inherit;font-color: inherit;",
            ),
            Field("comments", readonly=True, rows="5"),
            Field("date_manager_reviewed", readonly=True),
            Field(
                "submitted_by",
                readonly=True,
                style="color:black; height:auto; background-color:#e9ecef; opacity:1; font-weight: inherit; font-color: inherit;",
            ),
            Field("date_info_requested", readonly=True, hidden=True),
            Field("info_requested", readonly=True, hidden=True),
            Field("fund_center", style="height:auto"),
            Field("approved_by", style="height:auto"),
            Submit(
                "send_for_s32_approval",
                _("Send for S32 Approval"),
            ),
            Button(
                "request_info",
                _("Request Additional Information"),
                css_id="submit",
                css_class="btn btn-primary",
                data_toggle="modal",
                data_target="#request_info_modal",
                data_dismiss="modal",
            ),
            # hide the purchase button for now. It will be shown if the request is approved by an s32 approver.
            Button(
                "purchase",
                _("Record Purchase Information"),
                css_id="submit",
                css_class="btn btn-primary",
                data_toggle="modal",
                data_target="#purchase_modal",
                data_dismiss="modal",
                hidden=True,
            ),
            Button(
                "cancel",
                _("Cancel"),
                css_id="submit",
                css_class="btn btn-primary",
                onclick="window.location.href='/"
                + current_language
                + "/internal_ops/view'",
            ),
        )
        # append the Purchase Information button if the request is approved
        if (
            self.instance.status == "S32 approved"
            or self.instance.status == "Approuvé S32"
        ):
            self.helper.layout[24] = Button(
                "purchase",
                _("Record Purchase Information"),
                css_id="submit",
                css_class="btn btn-primary",
                data_toggle="modal",
                data_target="#purchase_modal",
                data_dismiss="modal",
            )
        # unhide the date requested and information requested if there is data associated with those fields.
        if self.instance.date_info_requested:
            self.helper.layout[17] = Field(
                "date_info_requested", readonly=True, hidden=False
            )
            self.fields["date_info_requested"].label = "Date Info Requested"
        if self.instance.info_requested:
            self.helper.layout[18] = Field(
                "info_requested", readonly=True, hidden=False
            )
            self.fields["info_requested"].label = "Info Requested"


class ViewPurchaseRequiredForm(ModelForm):
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
            "manager",
            "comments",
            "date_manager_reviewed",
            "submitted_by",
            "date_info_requested",
            "info_requested",
            "fund_center",
            "approved_by",
        ]
        labels = {
            "name": _("Name of Saas"),
            "url": _("URL"),
            "description": _("Description"),
            "cost": _("Cost"),
            "currency": _("Currency"),
            "frequency": _("Frequency"),
            "units": _("Units"),
            "level_of_subscription": _("Level of Subscription"),
            "duration": _("Duration"),
            "number_of_users": _("Number of Users"),
            "names_of_users": _("Names of Users"),
            "account_administrator": _("Account Administrator"),
            "backup_administrator": _("Backup Administrator"),
            "manager": _("Manager"),
            "comments": _("Comments"),
            "manager_approved": _("Manager Approved"),
            "Manager_denied": _("Manager Denied"),
            # "date_info_requested": _("Date Info Requested"),
            # "info_requested": _("Info Requested"),
            "submitted_by": _("Submitted By"),
            "fund_center": _("Fund Center"),
            "approved_by": _("S32 Approver"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "view_request_form"
        self.helper.form_class = "blueForms"
        # self.fields["date_info_requested"].label = False
        # self.fields["info_requested"].label = False
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
            Field(
                "manager",
                readonly=True,
                style="color:black; height:auto; background-color:#e9ecef; opacity:1;font-weight: inherit;font-color: inherit;",
            ),
            Field("comments", readonly=True, rows="5"),
            Field("date_manager_reviewed", readonly=True),
            Field(
                "submitted_by",
                readonly=True,
                style="color:black; height:auto; background-color:#e9ecef; opacity:1; font-weight: inherit; font-color: inherit;",
            ),
            Field("date_info_requested", readonly=True, hidden=True),
            Field("info_requested", readonly=True, hidden=True),
            Field("fund_center", style="height:auto"),
            Field("approved_by", style="height:auto"),
            Button(
                "request_info",
                _("Request Additional Information"),
                css_id="submit",
                css_class="btn btn-primary",
                data_toggle="modal",
                data_target="#request_info_modal",
                data_dismiss="modal",
            ),
            Button(
                "purchase",
                _("Record Purchase Information"),
                css_id="submit",
                css_class="btn btn-primary",
                data_toggle="modal",
                data_target="#purchase_modal",
                data_dismiss="modal",
            ),
            Button(
                "cancel",
                _("Cancel"),
                css_id="submit",
                css_class="btn btn-primary",
                onclick="window.location.href='/"
                + current_language
                + "/internal_ops/view'",
            ),
        )
        if self.instance.date_info_requested:
            self.helper.layout[17] = Field(
                "date_info_requested", readonly=True, hidden=False
            )
            self.fields["date_info_requested"].label = "Date Info Requested"
        if self.instance.info_requested:
            self.helper.layout[18] = Field(
                "info_requested", readonly=True, hidden=False
            )
            self.fields["info_requested"].label = "Info Requested"


class ViewOldPurchasedRequestsForm(ModelForm):
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
            "manager",
            "comments",
            "date_manager_reviewed",
            "manager_approved",
            "manager_denied",
            "submitted_by",
            "date_info_requested",
            "info_requested",
            "date_sent_to_s_32_approver",
            "s_32_review_date",
            "s_32_approved",
            "purchase_date",
            "purchase_amount",
            "purchase_method",
            "confirmation_number",
            "purchase_notes",
            "fund_center",
            "approved_by",
        ]
        labels = {
            "name": _("Name of Saas"),
            "url": _("URL"),
            "description": _("Description"),
            "cost": _("Cost"),
            "level_of_subscription": _("Level of Subscription"),
            "number_of_users": _("Number of Users"),
            "names_of_users": _("Names of Users"),
            "account_administrator": _("Account Administrator"),
            "backup_administrator": _("Backup Administrator"),
            "status": _("Current status"),
            "submitted_by": _("Submitted By"),
            "date_manager_reviewed": _("Date Manager reviewed the request"),
            "manager_approved": _("Manager Approved"),
            "manager_denied": _("Manager Denied"),
            "date_sent_to_s_32_approver": _("Date Sent to S32 Approver"),
            "fund_center": _("Fund Center"),
            "approved_by": _("S32 Approver"),
            "s_32_approved": _("S32 Approver approved"),
            "s_32_review_date": _("S32 Approver Review Date"),
            "purchase_date": _("Purchase Date"),
            "purchase_amount": _("Purchase Amount"),
            "purchase_method": _("Purchase Method"),
            "confirmation_number": _("Confirmation Number"),
            "purchase_notes": _("Purchase Notes"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "view_request_form"
        self.helper.form_class = "blueForms"
        # self.fields["date_info_requested"].label = False
        # self.fields["info_requested"].label = False
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
            Field(
                "manager",
                readonly=True,
                style="color:black; height:auto; background-color:#e9ecef; opacity:1;font-weight: inherit;font-color: inherit;",
            ),
            Field("comments", readonly=True, rows="5"),
            Field("date_manager_reviewed", readonly=True),
            Field("manager_approved", readonly=True),
            Field("manager_denied", readonly=True),
            Field(
                "submitted_by",
                readonly=True,
                style="color:black; height:auto; background-color:#e9ecef; opacity:1; font-weight: inherit; font-color: inherit;",
            ),
            Field("date_info_requested", readonly=True, hidden=True),
            Field("info_requested", readonly=True, hidden=True),
            Field("date_sent_to_s_32_approver", readonly=True),
            Field("s_32_review_date", readonly=True),
            Field("s_32_approved", readonly=True),
            Field("purchase_date", readonly=True),
            Field("purchase_amount", readonly=True),
            Field("purchase_method", readonly=True),
            Field("confirmation_number", readonly=True),
            Field("purchase_notes", readonly=True),
            Field(
                "fund_center",
                readonly=True,
                style="color:black; background-color:#e9ecef; opacity:1;font-weight: inherit;font-color: inherit;",
            ),
            Field(
                "approved_by",
                readonly=True,
                style="color:black; height:auto; background-color:#e9ecef; opacity:1;font-weight: inherit;font-color: inherit;",
            ),
            Button(
                "cancel",
                _("Cancel"),
                css_id="submit",
                css_class="btn btn-primary",
                onclick="window.location.href='/"
                + current_language
                + "/internal_ops/view'",
            ),
        )
        if self.instance.date_info_requested:
            self.helper.layout[19] = Field(
                "date_info_requested", readonly=True, hidden=False
            )
            self.fields["date_info_requested"].label = "Date Info Requested"
        if self.instance.info_requested:
            self.helper.layout[20] = Field(
                "info_requested", readonly=True, hidden=False
            )
            self.fields["info_requested"].label = "Info Requested"


class ViewOldS32ApprovedRequestsForm(ModelForm):
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
            "manager",
            "comments",
            "submitted_by",
            "date_manager_reviewed",
            "manager_approved",
            "manager_denied",
            "date_sent_to_s_32_approver",
            "date_info_requested",
            "info_requested",
            "fund_center",
            "approved_by",
        ]
        labels = {
            "name": _("Name of Saas"),
            "url": _("URL"),
            "submitted_by": _("Submitted By"),
            "level_of_subscription": _("Level of Subscription"),
            "number_of_users": _("Number of Users"),
            "names_of_users": _("Names of Users"),
            "account_administrator": _("Account Administrator"),
            "backup_administrator": _("Backup Administrator"),
            "status": _("Current Status"),
            "date_manager_reviewed": _("Date Manager reviewed the request"),
            "manager_approved": _("Manager Approved"),
            "manager_denied": _("Manager Denied"),
            "date_sent_to_s_32_approver": _("Date Sent to S32 Approver"),
            "fund_center": _("Fund Center"),
            "approved_by": _("S32 Approver"),
            "s_32_approved": _("S32 Approver approved"),
            "s_32_review_date": _("S32 Approver Review Date"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "view_request_form"
        self.helper.form_class = "blueForms"
        # self.fields["date_info_requested"].label = False
        # self.fields["info_requested"].label = False
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
            Field("number_of_users", readonly=True),
            Field("names_of_users", readonly=True),
            Field("account_administrator", readonly=True),
            Field("backup_administrator", readonly=True),
            Field(
                "manager",
                readonly=True,
                style="color:black; height:auto; background-color:#e9ecef; opacity:1;font-weight: inherit;font-color: inherit;",
            ),
            Field("comments", readonly=True, rows="5"),
            Field("date_manager_reviewed", readonly=True),
            Field("manager_approved", readonly=True),
            Field("manager_denied", readonly=True),
            Field(
                "submitted_by",
                readonly=True,
                style="color:black; height:auto; background-color:#e9ecef; opacity:1; font-weight: inherit; font-color: inherit;",
            ),
            Field("date_info_requested", readonly=True, hidden=True),
            Field("info_requested", readonly=True, hidden=True),
            Field("date_sent_to_s_32_approver", readonly=True),
            Field("fund_center", readonly=True, style="height:auto"),
            Field("approved_by", readonly=True, style="height:auto"),
            Button(
                "cancel",
                _("Cancel"),
                css_id="submit",
                css_class="btn btn-primary",
                onclick="history.back()",
            ),
        )
        if self.instance.date_info_requested:
            self.helper.layout[20] = Field(
                "date_info_requested", readonly=True, hidden=False
            )
            self.fields["date_info_requested"].label = "Date Info Requested"
        if self.instance.info_requested:
            self.helper.layout[21] = Field(
                "info_requested", readonly=True, hidden=False
            )
            self.fields["info_requested"].label = "Info Requested"
