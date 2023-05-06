from notifications_python_client.notifications import NotificationsAPIClient
from django.utils.translation import gettext as _
import os

# This contains common utility functions used by the application


# Initialize the Notify client and create an instance
def get_notify_client():
    return NotificationsAPIClient(
        os.getenv("NOTIFY_API_KEY"), base_url=os.getenv("NOTIFY_URL")
    )


# Use Notify to send emails
def send_email(email_address, template_id, details):
    print(
        "email_address: ",
        email_address,
        "template_id: ",
        template_id,
        "details: ",
        details,
    )
    try:
        notifications_client = get_notify_client()
        notifications_client.send_email_notification(
            email_address=email_address,
            template_id=template_id,
            personalisation=details,
        )
    except Exception as e:
        print(e)
        raise Exception(_("There was an error sending the email."))


# Get the current site domain
def get_current_site(request):
    return request.build_absolute_uri("/")
