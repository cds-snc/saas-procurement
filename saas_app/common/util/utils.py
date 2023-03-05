from notifications_python_client.notifications import NotificationsAPIClient
from django.contrib.sites.models import Site
import os

# This contains common utility functions used by the application

# Initialize the Notify client and create an instance
def get_notify_client():
    return NotificationsAPIClient(
        os.getenv("NOTIFY_API_KEY"), base_url=os.getenv("NOTIFY_URL")
    )
    
# Use Notify to send emails
def send_email(email_address, template_id, details):
    notifications_client = get_notify_client()
    notifications_client.send_email_notification(
        email_address=email_address, template_id=template_id, personalisation=details
    )


# Get the current site domain
def get_current_site(request):
    current_site = Site.objects.get_current()
    return current_site.domain
