from notifications_python_client.notifications import NotificationsAPIClient
import os


def send_notification(self):
    notifications_client = NotificationsAPIClient(
        os.getenv("NOTIFY_API_KEY"), base_url="https://api.notification.canada.ca"
    )
    notifications_client.send_email_notification(
        email_address="sylvia.mclaughlin@cds-snc.ca",
        template_id=os.getenv("APPROVAL_REQUEST_TEMPLATE_ID"),
        personalisation={"name": "Sylvia"},
    )
