from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class SubmitRequestForm(forms.Form):
    name = forms.CharField(
        label="What is the name of the Saas?", max_length=100, required=True
    )
    url = forms.URLField(label="Please provide the URL", max_length=100, required=True)
    description = forms.CharField(
        label="Provide a description and rationale for why you would like to request the SaaS.",
        widget=forms.Textarea,
        required=True,
    )
    cost = forms.CharField(
        label="What is the monthly or yearly cost (CAD or USD)?",
        max_length=100,
        required=True,
    )
    level_of_subscription = forms.CharField(
        label="What level of subscription are you requesting?",
        max_length=100,
        required=True,
    )
    number_of_users = forms.IntegerField(
        label="Please share the number of users", required=True
    )
    names_of_users = forms.CharField(
        label="Please share the names of the users",
        widget=forms.Textarea,
        required=True,
    )
    account_administrator = forms.CharField(
        label="Who will be the account administrator?", max_length=100, required=True
    )
    backup_administrator = forms.CharField(
        label="Who will be the backup administrator?", max_length=100, required=True
    )
    approver = forms.CharField(
        label="Who is the Product Manager or People Manager that will approve this SaaS request?",
        max_length=100,
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "submit_request_form"
        self.helper.form_class = "blueForms"
        self.helper.form_method = "post"
        self.helper.form_action = "submit_saas_form"

        self.helper.add_input(Submit("submit", "Submit"))
