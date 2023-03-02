from django.test import TestCase
from .models import SaasRequest, User, Users, Roles

# Unit tests to test the models and views of the saas_app application.
class SubmitRequestTestCase(TestCase):
    # Set up a model with the required fields.
    def setUp(self):
        role = Roles.objects.create(name="Test Name", description="Test Description")
        auth_user = User.objects.create_user(username="Test User", password="Test Password")
        approver = Users.objects.create(user=auth_user, first_name="Test First Name", last_name="Test Last Name", title="Test Title", business_unit="Test Business Unit")
        approver.user_roles.add(role)
        logged_user = User.objects.create_user(username="Test User 2", password="Test Password 2")
        SaasRequest.objects.create(name="Test Name", url="http://www.testurl.com", description="Test Description", cost="Test Cost", level_of_subscription="Test Level of Subscription", number_of_users=1, names_of_users="Test Names of Users", account_administrator="Test Account Administrator", backup_administrator="Test Backup Administrator", approver=approver, submitted_by=logged_user)
    
    # test that the model was created correctly    
    def test_saas_request(self):
        auth_user = User.objects.get(username="Test User")
        approver = Users.objects.get(user=auth_user)
        logged_user = User.objects.get(username="Test User 2")
        saas_request = SaasRequest.objects.get(name="Test Name")
        self.assertEqual(saas_request.url, "http://www.testurl.com")
        self.assertEqual(saas_request.description, "Test Description")
        self.assertEqual(saas_request.cost, "Test Cost")
        self.assertEqual(saas_request.level_of_subscription, "Test Level of Subscription")
        self.assertEqual(saas_request.number_of_users, 1)
        self.assertEqual(saas_request.names_of_users, "Test Names of Users")
        self.assertEqual(saas_request.account_administrator, "Test Account Administrator")
        self.assertEqual(saas_request.backup_administrator, "Test Backup Administrator")
        self.assertEqual(saas_request.approver, approver)
        self.assertEqual(saas_request.submitted_by, logged_user)
        
        
    # Test the lengths of the fields in the models
    def test_saas_request_max_length_fields(self):
        saas_request = SaasRequest.objects.get(name="Test Name")
        self.assertEqual(saas_request._meta.get_field('name').max_length, 100)
        self.assertEqual(saas_request._meta.get_field('url').max_length, 100)
        self.assertEqual(saas_request._meta.get_field('description').max_length, 500)
        self.assertEqual(saas_request._meta.get_field('cost').max_length, 100)
        self.assertEqual(saas_request._meta.get_field('level_of_subscription').max_length, 100)
        self.assertEqual(saas_request._meta.get_field('names_of_users').max_length, 500)
        self.assertEqual(saas_request._meta.get_field('number_of_users').max_length, None)
        self.assertEqual(saas_request._meta.get_field('account_administrator').max_length, 100)
        self.assertEqual(saas_request._meta.get_field('backup_administrator').max_length, 100)
        
    # Test that the string representation of the model is correctly returned
    def test_saas_request_string_representation(self):
        saas_request = SaasRequest.objects.get(name="Test Name")
        self.assertEqual(str(saas_request), "Test Name")
