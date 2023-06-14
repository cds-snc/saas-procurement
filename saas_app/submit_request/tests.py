from django.test import TestCase
from .models import SaasRequest, User, Users, Currency, Frequency
from user.models import Roles
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
        manager = Users.objects.create(
            user=auth_user,
            first_name="Test First Name",
            last_name="Test Last Name",
            title="Test Title",
            business_unit="Test Business Unit",
        )
        manager.user_roles.add(role)
        logged_user = User.objects.create_user(
            username="Test User 2", password="Test Password 2"
        )
        currency = Currency.objects.create(currency="CDN")
        frequency = Frequency.objects.create(frequency="Yearly")
        SaasRequest.objects.create(
            name="Test Name",
            url="http://www.testurl.com",
            description="Test Description",
            cost="Test Cost",
            currency=currency,
            frequency=frequency,
            units=1,
            duration="Test Duration",
            level_of_subscription="Test Level of Subscription",
            number_of_users=1,
            names_of_users="Test Names of Users",
            account_administrator="Test Account Administrator",
            backup_administrator="Test Backup Administrator",
            manager=manager,
            comments="Test Comments",
            submitted_by=logged_user,
            manager_approved=False,
        )

    # test that the model was created correctly
    def test_saas_request(self):
        auth_user = User.objects.get(username="Test User")
        manager = Users.objects.get(user=auth_user)
        logged_user = User.objects.get(username="Test User 2")
        saas_request = SaasRequest.objects.get(name="Test Name")
        frequency = Frequency.objects.get(frequency="Yearly")
        currency = Currency.objects.get(currency="CDN")
        self.assertEqual(saas_request.url, "http://www.testurl.com")
        self.assertEqual(saas_request.description, "Test Description")
        self.assertEqual(saas_request.cost, "Test Cost")
        self.assertEqual(saas_request.currency, currency)
        self.assertEqual(saas_request.frequency, frequency)
        self.assertEqual(saas_request.units, 1)
        self.assertEqual(saas_request.duration, "Test Duration")
        self.assertEqual(
            saas_request.level_of_subscription, "Test Level of Subscription"
        )
        self.assertEqual(saas_request.number_of_users, 1)
        self.assertEqual(saas_request.names_of_users, "Test Names of Users")
        self.assertEqual(
            saas_request.account_administrator, "Test Account Administrator"
        )
        self.assertEqual(saas_request.backup_administrator, "Test Backup Administrator")
        self.assertEqual(saas_request.manager, manager)
        self.assertEqual(saas_request.comments, "Test Comments")
        self.assertEqual(saas_request.submitted_by, logged_user)
        mocked_date = datetime.datetime(2020, 1, 1, 0, 0, 0)
        saas_request.date_submitted = mocked_date
        self.assertEqual(saas_request.date_submitted, mocked_date)
        self.assertEqual(saas_request.manager_approved, False)

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
            saas_request._meta.get_field("manager_approved").max_length, None
        )
        self.assertEqual(
            saas_request._meta.get_field("currency").max_length, None
        )
        self.assertEqual(
            saas_request._meta.get_field("frequency").max_length, None
        )
        self.assertEqual(
            saas_request._meta.get_field("units").max_length, 100
        )
        self.assertEqual(
            saas_request._meta.get_field("duration").max_length, 100
        )
        self.assertEqual(
            saas_request._meta.get_field("comments").max_length, 5000
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
            form.fields["name"].label is None or form.fields["name"].label == "Name"
        )

    # Test the url label of the form
    def test_url_label(self):
        form = SubmitRequestForm()
        self.assertTrue(
            form.fields["url"].label is None or form.fields["url"].label == "Url"
        )

    # Test the description label of the form
    def test_description_label(self):
        form = SubmitRequestForm()
        self.assertTrue(
            form.fields["description"].label is None
            or form.fields["description"].label == "Description"
        )

    # Test the cost label of the form
    def test_cost_label(self):
        form = SubmitRequestForm()
        self.assertTrue(
            form.fields["cost"].label is None or form.fields["cost"].label == "Cost"
        )

    # Test the currency label of the form
    def test_currency_label(self):
        form = SubmitRequestForm()
        self.assertTrue(
            form.fields["currency"].label is None or form.fields["currency"].label == "Currency"
        )
        
    # Test the frequency label of the form
    def test_frequency_label(self):
        form = SubmitRequestForm()
        self.assertTrue(
            form.fields["frequency"].label is None or form.fields["frequency"].label == "Frequency"
        )
    # Test units label of the form
    def test_units_label(self):
        form = SubmitRequestForm()
        self.assertTrue(
            form.fields["units"].label is None or form.fields["units"].label == "Units"
        )
        
    # Test duration label of the form
    def test_duration_label(self):
        form = SubmitRequestForm()
        self.assertTrue(
            form.fields["duration"].label is None or form.fields["duration"].label == "Duration"
        )
        
    # Test the comments label of the form
    def test_comments_label(self):
        form = SubmitRequestForm()
        self.assertTrue(
            form.fields["comments"].label is None or form.fields["comments"].label == "Comments"
        )
        
    # Test the level of subscription label of the form
    def test_level_of_subscription_label(self):
        form = SubmitRequestForm()
        self.assertTrue(
            form.fields["level_of_subscription"].label is None
            or form.fields["level_of_subscription"].label == "Level of subscription"
        )

    # Test the number of users label of the form
    def test_number_of_users_label(self):
        form = SubmitRequestForm()
        self.assertTrue(
            form.fields["number_of_users"].label is None
            or form.fields["number_of_users"].label == "Number of users"
        )

    # Test the names of users label of the form
    def test_names_of_users_label(self):
        form = SubmitRequestForm()
        self.assertTrue(
            form.fields["names_of_users"].label is None
            or form.fields["names_of_users"].label == "Names of users"
        )

    # Test the account administrator label of the form
    def test_account_administrator_label(self):
        form = SubmitRequestForm()
        self.assertTrue(
            form.fields["account_administrator"].label is None
            or form.fields["account_administrator"].label == "Account administrator"
        )

    # Test the backup administrator label of the form
    def test_backup_administrator_label(self):
        form = SubmitRequestForm()
        self.assertTrue(
            form.fields["backup_administrator"].label is None
            or form.fields["backup_administrator"].label == "Backup administrator"
        )


class TestSubmitRequestViews(TestCase):
    # Test that the submit request page is accessible
    def test_submit_request_page(self):
        response = self.client.get("/en/submit_request")
        self.assertEqual(response.status_code, 301)

    # Test that the view request page is accessible and redirects properly
    def test_view_request_page(self):
        response = self.client.get("/en/submit_request/view")
        self.assertEqual(response.status_code, 301)
