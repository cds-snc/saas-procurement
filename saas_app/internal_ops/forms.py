from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Button, Field
from django.forms import ModelForm
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
            "name": "Name",
            "url": "URL",
            "description": "Description",
            "cost": "Cost",
            "level_of_subscription": "Level of Subscription",
            "number_of_users": "Number of Users",
            "names_of_users": "Names of Users",
            "account_administrator": "Account Administrator",
            "backup_administrator": "Backup Administrator",
            "manager": "Manager",
            "date_manager_reviewed": "Date Manager Approved the request",
            "submitted_by": "Submitted By",
            "fund_center": "Fund Center",
            "approved_by": "S32 Approver",
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
                "Save",
            ),
            Submit("send_for_s32_approval", "Send for S32 Approval"),
            # place holder for now
            # Button(
            #     "request_info",
            #     "Request Additional Information",
            #     css_id="submit",
            #     css_class="btn btn-primary btn-lg",
            #     data_toggle="modal",
            #     data_target="#request_info_modal",
            #     data_dismiss="modal",
            # ),
            # Submit(
            #     "purchase",
            #     "Record Purchase Information",
            # ),
            Button(
                "cancel",
                "Cancel",
                css_id="submit",
                css_class="btn btn-primary btn-lg",
                onclick="history.back()",
            ),
        )
