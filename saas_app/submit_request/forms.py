from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Button
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
            "level_of_subscription",
            "number_of_users",
            "names_of_users",
            "account_administrator",
            "backup_administrator",
            "manager",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "submit_request_form"
        self.helper.form_class = "blueForms"
        self.helper.form_method = "post"
        self.helper.form_action = "submit_saas_form"
        self.helper.add_input(Submit("submit", "Submit", css_class="btn btn-primary"))
        self.helper.add_input(
            Button(
                "cancel",
                "Cancel",
                css_id="submit",
                css_class="btn btn-primary btn-lg",
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
            "level_of_subscription",
            "number_of_users",
            "names_of_users",
            "account_administrator",
            "backup_administrator",
            "manager",
        ]

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
            "level_of_subscription",
            "number_of_users",
            "names_of_users",
            "account_administrator",
            "backup_administrator",
            "manager",
            Submit("save", "Save changes"),
            Submit(
                "delete",
                "Delete",
                onclick="return confirm('Are you sure you want to delete this saas request?');",
            ),
            Button(
                "cancel",
                "Cancel",
                css_id="submit",
                css_class="btn btn-primary btn-lg",
                onclick="history.back()",
            ),
        )
