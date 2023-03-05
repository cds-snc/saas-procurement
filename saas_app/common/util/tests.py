import os
import pytest
from unittest.mock import MagicMock, patch, Mock
from django.test import TestCase
import common.util.utils as utils

# Tests to test the utility functions

class UtilsTestCase(TestCase):    
    # Test that the get_current_site function returns the correct domain
    def test_get_current_site(self):
        request = MagicMock()
        request.get_host.return_value = "example.com"
        self.assertEqual(utils.get_current_site(request), "example.com")
   
   # Test that the environment variables are set
    def test_notify_client_environment_variables(self):
       utils.get_notify_client()
       self.assertIn("NOTIFY_API_KEY", os.environ)
       self.assertIn("NOTIFY_URL", os.environ)
    
    # Test that the get_notify_client function returns the correct instance       
    def test_notify_client_correct_instance(self):
        notify_client = utils.get_notify_client()
        self.assertIsInstance(notify_client, utils.NotificationsAPIClient)
    
    # Test that the correct base_url is set for the Notify client    
    def test_notify_client_correct_url(self):
        notify_client = utils.get_notify_client()
        self.assertEqual(notify_client.base_url, os.getenv("NOTIFY_URL"))
    
    # Test that the notify client is initialized and is called once       
    @patch("common.util.utils.NotificationsAPIClient")
    def test_get_notify_client(self, mock_notify_client):
        utils.get_notify_client()
        mock_notify_client.assert_called_once_with(
            os.getenv("NOTIFY_API_KEY"), base_url=os.getenv("NOTIFY_URL")
        )
    
    # Test that the send_email function calls the correct function on the notify client    
    @patch("common.util.utils.get_notify_client")
    def test_send_email(self, mock_get_notify_client):
        client = MagicMock()
        mock_get_notify_client.return_value = client
        email_address = "foo@foo.com"
        template_id = "123"
        details = {"foo": "bar"}
        utils.send_email(email_address, template_id, details)
        client.send_email_notification.assert_called_once_with(email_address = email_address, template_id = template_id, personalisation = details)
       