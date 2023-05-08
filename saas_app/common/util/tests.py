import os
from unittest.mock import MagicMock, patch
from django.test import TestCase
import common.util.utils as utils


# Tests to test the utility functions
class UtilsTestCase(TestCase):
    # Test that the get_current_site function returns the correct domain
    def test_get_current_site(self):
        request = MagicMock()
        request.build_absolute_uri.return_value = "http://example.com/"
        self.assertEqual(utils.get_current_site(request), "http://example.com/")

    # Test that the notify client is initialized and is called once
    @patch("common.util.utils.NotificationsAPIClient")
    def test_get_notify_client(self, mock_notify_client):
        utils.get_notify_client()
        mock_notify_client.assert_called_once_with(
            os.getenv("NOTIFY_API_KEY"), base_url=os.getenv("NOTIFY_URL")
        )

    # Test that the send_email function calls the correct function on the notify clientgit
    @patch("common.util.utils.get_notify_client")
    def test_send_email(self, mock_get_notify_client):
        client = MagicMock()
        mock_get_notify_client.return_value = client
        email_address = "foo@foo.com"
        template_id = "123"
        details = {"foo": "bar"}
        utils.send_email(email_address, template_id, details)
        client.send_email_notification.assert_called_once_with(
            email_address=email_address,
            template_id=template_id,
            personalisation=details,
        )
