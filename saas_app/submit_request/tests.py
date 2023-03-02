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
        SaasRequest.objects.create(name="Test Name", url="http://www.testurl.com", description="Test Description", cost="Test Cost", level_of_subscription="Test Level of Subscription", number_of_users=1, names_of_users="Test Names of Users", account_administrator="Test Account Administrator", backup_administrator="Test Backup Administrator", approver=approver)
    
    # test that the model was created correctly    
    def test_saas_request(self):
        auth_user = User.objects.get(username="Test User")
        approver = Users.objects.get(user=auth_user)
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
        
