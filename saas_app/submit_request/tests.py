from django.test import TestCase
from unittest.mock import MagicMock
from .models import SaasRequest, User, Users, Roles
from .forms import SubmitRequestForm
import datetime

# Unit tests to test the models and views of the saas_app application.


# Test class to test the SaasRequest model
class SubmitRequestModelTestCase(TestCase):
    # Set up a model with the required fields.
    def setUp(self):
        role = Roles.objects.create(name="Test Name", description="Test Description")
        auth_user = User.objects.create_user(
            username="Test User", password="Test Password"
        )
        approver = Users.objects.create(
            user=auth_user,
            first_name="Test First Name",
            last_name="Test Last Name",
            title="Test Title",
            business_unit="Test Business Unit",
        )
        approver.user_roles.add(role)
        logged_user = User.objects.create_user(
            username="Test User 2", password="Test Password 2"
        )        
        SaasRequest.objects.create(
            name="Test Name",
            url="http://www.testurl.com",
            description="Test Description",
            cost="Test Cost",
            level_of_subscription="Test Level of Subscription",
            number_of_users=1,
            names_of_users="Test Names of Users",
            account_administrator="Test Account Administrator",
            backup_administrator="Test Backup Administrator",
            approver=approver,
            submitted_by=logged_user,
            approved=False,
        )

    # test that the model was created correctly
    def test_saas_request(self):
        auth_user = User.objects.get(username="Test User")
        approver = Users.objects.get(user=auth_user)
        logged_user = User.objects.get(username="Test User 2")
        saas_request = SaasRequest.objects.get(name="Test Name")
        self.assertEqual(saas_request.url, "http://www.testurl.com")
        self.assertEqual(saas_request.description, "Test Description")
        self.assertEqual(saas_request.cost, "Test Cost")
        self.assertEqual(
            saas_request.level_of_subscription, "Test Level of Subscription"
        )
        self.assertEqual(saas_request.number_of_users, 1)
        self.assertEqual(saas_request.names_of_users, "Test Names of Users")
        self.assertEqual(
            saas_request.account_administrator, "Test Account Administrator"
        )
        self.assertEqual(saas_request.backup_administrator, "Test Backup Administrator")
        self.assertEqual(saas_request.approver, approver)
        self.assertEqual(saas_request.submitted_by, logged_user)
        mocked_date = datetime.datetime(2020, 1, 1, 0, 0, 0)
        saas_request.date_submitted = mocked_date
        self.assertEqual(saas_request.date_submitted, mocked_date)
        self.assertEqual(saas_request.approved, False)

    # Test the lengths of the fields in the models
    def test_saas_request_max_length_fields(self):
        saas_request = SaasRequest.objects.get(name="Test Name")
        self.assertEqual(saas_request._meta.get_field("name").max_length, 100)
        self.assertEqual(saas_request._meta.get_field("url").max_length, 100)
        self.assertEqual(saas_request._meta.get_field("description").max_length, 500)
        self.assertEqual(saas_request._meta.get_field("cost").max_length, 100)
        self.assertEqual(
            saas_request._meta.get_field("level_of_subscription").max_length, 100
        )
        self.assertEqual(saas_request._meta.get_field("names_of_users").max_length, 500)
        self.assertEqual(
            saas_request._meta.get_field("number_of_users").max_length, None
        )
        self.assertEqual(
            saas_request._meta.get_field("account_administrator").max_length, 100
        )
        self.assertEqual(
            saas_request._meta.get_field("backup_administrator").max_length, 100
        )
        self.assertEqual(
            saas_request._meta.get_field("date_submitted").max_length, None
        )
        self.assertEqual(
            saas_request._meta.get_field("approved").max_length, None
        )

    # Test that the string representation of the model is correctly returned
    def test_saas_request_string_representation(self):
        saas_request = SaasRequest.objects.get(name="Test Name")
        self.assertEqual(str(saas_request), "Test Name")


# Test class to test out the submit request form
class SubmitRequestFormTest(TestCase):
    # Test the name label of the form
    def test_name_label(self):
        form = SubmitRequestForm()
        self.assertTrue(
            form.fields["name"].label == None or form.fields["name"].label == "Name"
        )

    # Test the url label of the form
    def test_url_label(self):
        form = SubmitRequestForm()
        self.assertTrue(
            form.fields["url"].label == None or form.fields["url"].label == "Url"
        )

    # Test the description label of the form
    def test_description_label(self):
        form = SubmitRequestForm()
        self.assertTrue(
            form.fields["description"].label == None
            or form.fields["description"].label == "Description"
        )

    # Test the cost label of the form
    def test_cost_label(self):
        form = SubmitRequestForm()
        self.assertTrue(
            form.fields["cost"].label == None or form.fields["cost"].label == "Cost"
        )

    # Test the level of subscription label of the form
    def test_level_of_subscription_label(self):
        form = SubmitRequestForm()
        self.assertTrue(
            form.fields["level_of_subscription"].label == None
            or form.fields["level_of_subscription"].label == "Level of subscription"
        )

    # Test the number of users label of the form
    def test_number_of_users_label(self):
        form = SubmitRequestForm()
        self.assertTrue(
            form.fields["number_of_users"].label == None
            or form.fields["number_of_users"].label == "Number of users"
        )

    # Test the names of users label of the form
    def test_names_of_users_label(self):
        form = SubmitRequestForm()
        self.assertTrue(
            form.fields["names_of_users"].label == None
            or form.fields["names_of_users"].label == "Names of users"
        )

    # Test the account administrator label of the form
    def test_account_administrator_label(self):
        form = SubmitRequestForm()
        self.assertTrue(
            form.fields["account_administrator"].label == None
            or form.fields["account_administrator"].label == "Account administrator"
        )

    # Test the backup administrator label of the form
    def test_backup_administrator_label(self):
        form = SubmitRequestForm()
        self.assertTrue(
            form.fields["backup_administrator"].label == None
            or form.fields["backup_administrator"].label == "Backup administrator"
        )

class TestSubmitRequestViews(TestCase):
    # Test that the submit request page is accessible
    def test_submit_request_page(self):
        response = self.client.get("/submit_request")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "saas_request.html")

    # Test that the view request page is accessible
    def test_view_request_page(self):
        response = self.client.get("/view_request")
        self.assertEqual(response.status_code, 301)
