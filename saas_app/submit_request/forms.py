from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm
from .models import SaasRequest
from saas_app.services import NotifyService
import os


# Submit Saas Request Form
class SubmitRequestForm(ModelForm):
    # Form is generated from the database fields. 
    class Meta:
        model = SaasRequest
        fields = ['name', 'url', 'description', 'cost', 'level_of_subscription', 'number_of_users', 'names_of_users', 'account_administrator', 'backup_administrator', 'approver']
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "submit_request_form"
        self.helper.form_class = "blueForms"
        self.helper.form_method = "post"
        self.helper.form_action = "submit_saas_form"

        self.helper.add_input(Submit("submit", "Submit"))

        def send_mail(notify_service: NotifyService(os.getenv("NOTIFY_API_KEY"), os.getenv("NOTIFY_API_URL")), email_address, template_id, details):
            # Send an email to the requestor or approver
            notify_service.send_email(email_address, template_id, details)
                                 