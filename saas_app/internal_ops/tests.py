from django.test import TestCase
from django.utils import timezone
from submit_request.models import SaasRequest, User, Users, Currency, Frequency
from user.models import Roles
from .models import FundCenter
from .forms import (
    ViewS32RequestForm,
    ViewPurchaseRequiredForm,
    ViewOldPurchasedRequestsForm,
    ViewOldS32ApprovedRequestsForm,
)
import datetime

# Unit tests to test the models and views of the internal ops saas_app application.


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
        currency = Currency.objects.create(
            currency="CDN", description="Test Description"
        )
        frequency = Frequency.objects.create(
            frequency="Yearly", description="Test Description"
        )
        manager.user_roles.add(role)
        logged_user = User.objects.create_user(
            username="Test User 2", password="Test Password 2"
        )
        fund_center = FundCenter.objects.create(
            name="Test Fund Center Name",
            number="Test Fund Center Number",
        )

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
            date_manager_reviewed=datetime.datetime(
                2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc
            ),
            date_info_requested=datetime.datetime(
                2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc
            ),
            info_requested="Test Info Requested",
            fund_center=fund_center,
            date_sent_to_s_32_approver=datetime.datetime(
                2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc
            ),
            s_32_review_date=datetime.datetime(
                2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc
            ),
            s_32_approved=True,
            purchase_date=datetime.datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
            purchase_amount=100,
            purchase_method="Test Purchase Method",
            confirmation_number="Test Confirmation Number",
            purchase_notes="Test Purchase Notes",
            approved_by=manager,
            manager=manager,
            comments="Test Comments",
            submitted_by=logged_user,
            manager_approved=True,
            manager_denied=False,
        )

    # test that the model was created correctly
    def test_saas_request(self):
        auth_user = User.objects.get(username="Test User")
        manager = Users.objects.get(user=auth_user)
        logged_user = User.objects.get(username="Test User 2")
        fund_center = FundCenter.objects.get(name="Test Fund Center Name")
        frequency = Frequency.objects.get(frequency="Yearly")
        currency = Currency.objects.get(currency="CDN")
        saas_request = SaasRequest.objects.get(name="Test Name")
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
        saas_request.date_manager_reviewed = mocked_date
        self.assertEqual(saas_request.date_manager_reviewed, mocked_date)
        saas_request.date_info_requested = mocked_date
        self.assertEqual(saas_request.date_info_requested, mocked_date)
        saas_request.date_sent_to_s_32_approver = mocked_date
        self.assertEqual(saas_request.date_sent_to_s_32_approver, mocked_date)
        saas_request.s_32_review_date = mocked_date
        self.assertEqual(saas_request.s_32_review_date, mocked_date)
        saas_request.purchase_date = mocked_date
        self.assertEqual(saas_request.purchase_date, mocked_date)
        self.assertEqual(saas_request.s_32_approved, True)
        self.assertEqual(saas_request.purchase_amount, 100)
        self.assertEqual(saas_request.purchase_method, "Test Purchase Method")
        self.assertEqual(saas_request.confirmation_number, "Test Confirmation Number")
        self.assertEqual(saas_request.purchase_notes, "Test Purchase Notes")
        self.assertEqual(saas_request.info_requested, "Test Info Requested")
        self.assertEqual(saas_request.fund_center, fund_center)
        self.assertEqual(saas_request.approved_by, manager)
        self.assertEqual(saas_request.manager_approved, True)
        self.assertEqual(saas_request.manager_denied, False)

    # Test the lengths of the fields in the models
    def test_saas_request_max_length_fields(self):
        saas_request = SaasRequest.objects.get(name="Test Name")
        self.assertEqual(saas_request._meta.get_field("name").max_length, 100)
        self.assertEqual(saas_request._meta.get_field("url").max_length, 100)
        self.assertEqual(saas_request._meta.get_field("description").max_length, 500)
        self.assertEqual(saas_request._meta.get_field("cost").max_length, 100)
        self.assertEqual(saas_request._meta.get_field("currency").max_length, None)
        self.assertEqual(saas_request._meta.get_field("frequency").max_length, None)
        self.assertEqual(saas_request._meta.get_field("units").max_length, None)
        self.assertEqual(saas_request._meta.get_field("duration").max_length, 100)
        self.assertEqual(saas_request._meta.get_field("comments").max_length, None)
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
            saas_request._meta.get_field("date_manager_reviewed").max_length, None
        )
        self.assertEqual(
            saas_request._meta.get_field("date_info_requested").max_length, None
        )
        self.assertEqual(
            saas_request._meta.get_field("info_requested").max_length, 5000
        )
        self.assertEqual(
            saas_request._meta.get_field("date_sent_to_s_32_approver").max_length, None
        )
        self.assertEqual(saas_request._meta.get_field("fund_center").max_length, None)
        self.assertEqual(saas_request._meta.get_field("approved_by").max_length, None)
        self.assertEqual(
            saas_request._meta.get_field("s_32_review_date").max_length, None
        )
        self.assertEqual(saas_request._meta.get_field("s_32_approved").max_length, None)
        self.assertEqual(saas_request._meta.get_field("purchase_date").max_length, None)
        self.assertEqual(
            saas_request._meta.get_field("purchase_amount").max_length, None
        )
        self.assertEqual(
            saas_request._meta.get_field("purchase_method").max_length, 100
        )
        self.assertEqual(
            saas_request._meta.get_field("confirmation_number").max_length, 100
        )
        self.assertEqual(saas_request._meta.get_field("purchase_notes").max_length, 500)

    # Test that the string representation of the model is correctly returned
    def test_saas_request_string_representation(self):
        saas_request = SaasRequest.objects.get(name="Test Name")
        self.assertEqual(str(saas_request), "Test Name")


# Test class to test out the submit request form
class ViewS32RequestFormTest(TestCase):
    # Test the name label of the form
    def test_name_label(self):
        form = ViewS32RequestForm()
        self.assertTrue(
            form.fields["name"].label is None
            or form.fields["name"].label == "Name of Saas"
        )

    # Test the url label of the form
    def test_url_label(self):
        form = ViewS32RequestForm()
        self.assertTrue(
            form.fields["url"].label is None or form.fields["url"].label == "URL"
        )

    # Test the description label of the form
    def test_description_label(self):
        form = ViewS32RequestForm()
        self.assertTrue(
            form.fields["description"].label is None
            or form.fields["description"].label == "Description"
        )

    # Test the cost label of the form
    def test_cost_label(self):
        form = ViewS32RequestForm()
        self.assertTrue(
            form.fields["cost"].label is None or form.fields["cost"].label == "Cost"
        )

    # Test the currency label of the form
    def test_currency_label(self):
        form = ViewS32RequestForm()
        self.assertTrue(
            form.fields["currency"].label is None
            or form.fields["currency"].label == "Currency"
        )

    # Test the frequency label of the form
    def test_frequency_label(self):
        form = ViewS32RequestForm()
        self.assertTrue(
            form.fields["frequency"].label is None
            or form.fields["frequency"].label == "Frequency"
        )

    # Test units label of the form
    def test_units_label(self):
        form = ViewS32RequestForm()
        self.assertTrue(
            form.fields["units"].label is None or form.fields["units"].label == "Units"
        )

    # Test duration label of the form
    def test_duration_label(self):
        form = ViewS32RequestForm()
        self.assertTrue(
            form.fields["duration"].label is None
            or form.fields["duration"].label == "Duration"
        )

    # Test the comments label of the form
    def test_comments_label(self):
        form = ViewS32RequestForm()
        self.assertTrue(
            form.fields["comments"].label is None
            or form.fields["comments"].label == "Comments"
        )

    # Test the level of subscription label of the form
    def test_level_of_subscription_label(self):
        form = ViewS32RequestForm()
        self.assertTrue(
            form.fields["level_of_subscription"].label is None
            or form.fields["level_of_subscription"].label == "Level of Subscription"
        )

    # Test the number of users label of the form
    def test_number_of_users_label(self):
        form = ViewS32RequestForm()
        self.assertTrue(
            form.fields["number_of_users"].label is None
            or form.fields["number_of_users"].label == "Number of Users"
        )

    # Test the names of users label of the form
    def test_names_of_users_label(self):
        form = ViewS32RequestForm()
        self.assertTrue(
            form.fields["names_of_users"].label is None
            or form.fields["names_of_users"].label == "Names of Users"
        )

    # Test the account administrator label of the form
    def test_account_administrator_label(self):
        form = ViewS32RequestForm()
        self.assertTrue(
            form.fields["account_administrator"].label is None
            or form.fields["account_administrator"].label == "Account Administrator"
        )

    # Test the backup administrator label of the form
    def test_backup_administrator_label(self):
        form = ViewS32RequestForm()
        self.assertTrue(
            form.fields["backup_administrator"].label is None
            or form.fields["backup_administrator"].label == "Backup Administrator"
        )

    # Test the manager label of the form
    def test_manager_label(self):
        form = ViewS32RequestForm()
        self.assertTrue(
            form.fields["manager"].label is None
            or form.fields["manager"].label == "Manager"
        )

    # Test the manager label of the form
    def test_manager_reviewed_label(self):
        form = ViewS32RequestForm()
        self.assertTrue(
            form.fields["date_manager_reviewed"].label is None
            or form.fields["date_manager_reviewed"].label
            == "Date Manager reviewed the request"
        )

    # Test the submitted label of the form
    def test_submitted_by_label(self):
        form = ViewS32RequestForm()
        self.assertTrue(
            form.fields["submitted_by"].label is None
            or form.fields["submitted_by"].label == "Submitted By"
        )

    # Test the date info requested label of the form
    def test_date_info_requested_label(self):
        form = ViewS32RequestForm()
        self.assertTrue(
            form.fields["date_info_requested"].label is None
            or form.fields["date_info_requested"].label == "Date Info Requested"
        )

    # Test the info requested label of the form
    def test_info_requested_label(self):
        form = ViewS32RequestForm()
        self.assertTrue(
            form.fields["info_requested"].label is None
            or form.fields["info_requested"].label == "Info Requested"
        )

    # Test the fund center label of the form
    def test_fund_center_label(self):
        form = ViewS32RequestForm()
        self.assertTrue(
            form.fields["fund_center"].label is None
            or form.fields["fund_center"].label == "Fund Center"
        )

    # Test the approved by label of the form
    def test_approved_by_label(self):
        form = ViewS32RequestForm()
        self.assertTrue(
            form.fields["approved_by"].label is None
            or form.fields["approved_by"].label == "S32 Approver"
        )


# Test class to test out the view old purchase requests form
class ViewPurchaseRequiredFormTest(TestCase):
    # Test the name label of the form
    def test_name_label(self):
        form = ViewPurchaseRequiredForm()
        self.assertTrue(
            form.fields["name"].label is None
            or form.fields["name"].label == "Name of Saas"
        )

    # Test the url label of the form
    def test_url_label(self):
        form = ViewPurchaseRequiredForm()
        self.assertTrue(
            form.fields["url"].label is None or form.fields["url"].label == "URL"
        )

    # Test the description label of the form
    def test_description_label(self):
        form = ViewPurchaseRequiredForm()
        self.assertTrue(
            form.fields["description"].label is None
            or form.fields["description"].label == "Description"
        )

    # Test the cost label of the form
    def test_cost_label(self):
        form = ViewPurchaseRequiredForm()
        self.assertTrue(
            form.fields["cost"].label is None or form.fields["cost"].label == "Cost"
        )

    # Test the currency label of the form
    def test_currency_label(self):
        form = ViewPurchaseRequiredForm()
        self.assertTrue(
            form.fields["currency"].label is None
            or form.fields["currency"].label == "Currency"
        )

    # Test the frequency label of the form
    def test_frequency_label(self):
        form = ViewPurchaseRequiredForm()
        self.assertTrue(
            form.fields["frequency"].label is None
            or form.fields["frequency"].label == "Frequency"
        )

    # Test units label of the form
    def test_units_label(self):
        form = ViewPurchaseRequiredForm()
        self.assertTrue(
            form.fields["units"].label is None or form.fields["units"].label == "Units"
        )

    # Test duration label of the form
    def test_duration_label(self):
        form = ViewPurchaseRequiredForm()
        self.assertTrue(
            form.fields["duration"].label is None
            or form.fields["duration"].label == "Duration"
        )

    # Test the comments label of the form
    def test_comments_label(self):
        form = ViewPurchaseRequiredForm()
        self.assertTrue(
            form.fields["comments"].label is None
            or form.fields["comments"].label == "Comments"
        )

    # Test the level of subscription label of the form
    def test_level_of_subscription_label(self):
        form = ViewPurchaseRequiredForm()
        self.assertTrue(
            form.fields["level_of_subscription"].label is None
            or form.fields["level_of_subscription"].label == "Level of Subscription"
        )

    # Test the number of users label of the form
    def test_number_of_users_label(self):
        form = ViewPurchaseRequiredForm()
        self.assertTrue(
            form.fields["number_of_users"].label is None
            or form.fields["number_of_users"].label == "Number of Users"
        )

    # Test the names of users label of the form
    def test_names_of_users_label(self):
        form = ViewPurchaseRequiredForm()
        self.assertTrue(
            form.fields["names_of_users"].label is None
            or form.fields["names_of_users"].label == "Names of Users"
        )

    # Test the account administrator label of the form
    def test_account_administrator_label(self):
        form = ViewPurchaseRequiredForm()
        self.assertTrue(
            form.fields["account_administrator"].label is None
            or form.fields["account_administrator"].label == "Account Administrator"
        )

    # Test the backup administrator label of the form
    def test_backup_administrator_label(self):
        form = ViewPurchaseRequiredForm()
        self.assertTrue(
            form.fields["backup_administrator"].label is None
            or form.fields["backup_administrator"].label == "Backup Administrator"
        )

    # Test the manager label of the form
    def test_manager_label(self):
        form = ViewPurchaseRequiredForm()
        self.assertTrue(
            form.fields["manager"].label is None
            or form.fields["manager"].label == "Manager"
        )

    # Test the manager label of the form
    def test_manager_reviewed_label(self):
        form = ViewPurchaseRequiredForm()
        self.assertTrue(
            form.fields["date_manager_reviewed"].label is None
            or form.fields["date_manager_reviewed"].label
            == "Date Manager reviewed the request"
        )

    # Test the submitted label of the form
    def test_submitted_by_label(self):
        form = ViewPurchaseRequiredForm()
        self.assertTrue(
            form.fields["submitted_by"].label is None
            or form.fields["submitted_by"].label == "Submitted By"
        )

    # Test the date info requested label of the form
    def test_date_info_requested_label(self):
        form = ViewPurchaseRequiredForm()
        self.assertTrue(
            form.fields["date_info_requested"].label is None
            or form.fields["date_info_requested"].label == "Date Info Requested"
        )

    # Test the info requested label of the form
    def test_info_requested_label(self):
        form = ViewPurchaseRequiredForm()
        self.assertTrue(
            form.fields["info_requested"].label is None
            or form.fields["info_requested"].label == "Info Requested"
        )

    # Test the fund center label of the form
    def test_fund_center_label(self):
        form = ViewPurchaseRequiredForm()
        self.assertTrue(
            form.fields["fund_center"].label is None
            or form.fields["fund_center"].label == "Fund Center"
        )

    # Test the approved by label of the form
    def test_approved_by_label(self):
        form = ViewPurchaseRequiredForm()
        self.assertTrue(
            form.fields["approved_by"].label is None
            or form.fields["approved_by"].label == "S32 Approver"
        )


# Test class to test out the view old purchase requests form
class ViewOldPurchasedRequestsFormTest(TestCase):
    # Test the name label of the form
    def test_name_label(self):
        form = ViewOldPurchasedRequestsForm()
        self.assertTrue(
            form.fields["name"].label is None
            or form.fields["name"].label == "Name of Saas"
        )

    # Test the url label of the form
    def test_url_label(self):
        form = ViewOldPurchasedRequestsForm()
        self.assertTrue(
            form.fields["url"].label is None or form.fields["url"].label == "URL"
        )

    # Test the description label of the form
    def test_description_label(self):
        form = ViewOldPurchasedRequestsForm()
        self.assertTrue(
            form.fields["description"].label is None
            or form.fields["description"].label == "Description"
        )

    # Test the cost label of the form
    def test_cost_label(self):
        form = ViewOldPurchasedRequestsForm()
        self.assertTrue(
            form.fields["cost"].label is None or form.fields["cost"].label == "Cost"
        )

    # Test the currency label of the form
    def test_currency_label(self):
        form = ViewOldPurchasedRequestsForm()
        self.assertTrue(
            form.fields["currency"].label is None
            or form.fields["currency"].label == "Currency"
        )

    # Test the frequency label of the form
    def test_frequency_label(self):
        form = ViewOldPurchasedRequestsForm()
        self.assertTrue(
            form.fields["frequency"].label is None
            or form.fields["frequency"].label == "Frequency"
        )

    # Test units label of the form
    def test_units_label(self):
        form = ViewOldPurchasedRequestsForm()
        self.assertTrue(
            form.fields["units"].label is None or form.fields["units"].label == "Units"
        )

    # Test duration label of the form
    def test_duration_label(self):
        form = ViewOldPurchasedRequestsForm()
        self.assertTrue(
            form.fields["duration"].label is None
            or form.fields["duration"].label == "Duration"
        )

    # Test the comments label of the form
    def test_comments_label(self):
        form = ViewOldPurchasedRequestsForm()
        self.assertTrue(
            form.fields["comments"].label is None
            or form.fields["comments"].label == "Comments"
        )

    # Test the level of subscription label of the form
    def test_level_of_subscription_label(self):
        form = ViewOldPurchasedRequestsForm()
        self.assertTrue(
            form.fields["level_of_subscription"].label is None
            or form.fields["level_of_subscription"].label == "Level of Subscription"
        )

    # Test the number of users label of the form
    def test_number_of_users_label(self):
        form = ViewOldPurchasedRequestsForm()
        self.assertTrue(
            form.fields["number_of_users"].label is None
            or form.fields["number_of_users"].label == "Number of Users"
        )

    # Test the names of users label of the form
    def test_names_of_users_label(self):
        form = ViewOldPurchasedRequestsForm()
        self.assertTrue(
            form.fields["names_of_users"].label is None
            or form.fields["names_of_users"].label == "Names of Users"
        )

    # Test the account administrator label of the form
    def test_account_administrator_label(self):
        form = ViewOldPurchasedRequestsForm()
        self.assertTrue(
            form.fields["account_administrator"].label is None
            or form.fields["account_administrator"].label == "Account Administrator"
        )

    # Test the backup administrator label of the form
    def test_backup_administrator_label(self):
        form = ViewOldPurchasedRequestsForm()
        self.assertTrue(
            form.fields["backup_administrator"].label is None
            or form.fields["backup_administrator"].label == "Backup Administrator"
        )

    # Test the manager label of the form
    def test_manager_label(self):
        form = ViewOldPurchasedRequestsForm()
        self.assertTrue(
            form.fields["manager"].label is None
            or form.fields["manager"].label == "Manager"
        )

    # Test the manager label of the form
    def test_manager_reviewed_label(self):
        form = ViewOldPurchasedRequestsForm()
        self.assertTrue(
            form.fields["date_manager_reviewed"].label is None
            or form.fields["date_manager_reviewed"].label
            == "Date Manager reviewed the request"
        )

    # Test the manager approved label of the form
    def test_manager_approved_label(self):
        form = ViewOldPurchasedRequestsForm()
        self.assertTrue(
            form.fields["manager_approved"].label is None
            or form.fields["manager_approved"].label == "Manager Approved"
        )

    # Test the manager denied label of the form
    def test_manager_denied_label(self):
        form = ViewOldPurchasedRequestsForm()
        self.assertTrue(
            form.fields["manager_denied"].label is None
            or form.fields["manager_denied"].label == "Manager Denied"
        )

    # Test the submitted label of the form
    def test_submitted_by_label(self):
        form = ViewOldPurchasedRequestsForm()
        self.assertTrue(
            form.fields["submitted_by"].label is None
            or form.fields["submitted_by"].label == "Submitted By"
        )

    # Test the date info requested label of the form
    def test_date_info_requested_label(self):
        form = ViewOldPurchasedRequestsForm()
        self.assertTrue(
            form.fields["date_info_requested"].label is None
            or form.fields["date_info_requested"].label == "Date Info Requested"
        )

    # Test the info requested label of the form
    def test_info_requested_label(self):
        form = ViewOldPurchasedRequestsForm()
        self.assertTrue(
            form.fields["info_requested"].label is None
            or form.fields["info_requested"].label == "Info Requested"
        )

    # Test the fund center label of the form
    def test_fund_center_label(self):
        form = ViewOldPurchasedRequestsForm()
        self.assertTrue(
            form.fields["fund_center"].label is None
            or form.fields["fund_center"].label == "Fund Center"
        )

    # Test the approved by label of the form
    def test_approved_by_label(self):
        form = ViewOldPurchasedRequestsForm()
        self.assertTrue(
            form.fields["approved_by"].label is None
            or form.fields["approved_by"].label == "S32 Approver"
        )

    # Test the date sent to s32 approval label of the form
    def test_date_sent_to_s_32_approver_label(self):
        form = ViewOldPurchasedRequestsForm()
        self.assertTrue(
            form.fields["date_sent_to_s_32_approver"].label is None
            or form.fields["date_sent_to_s_32_approver"].label
            == "Date Sent to S32 Approver"
        )

    # Test the date sent to s32 review date label of the form
    def test_s32_review_date_label(self):
        form = ViewOldPurchasedRequestsForm()
        self.assertTrue(
            form.fields["s_32_review_date"].label is None
            or form.fields["s_32_review_date"].label == "S32 Approver Review Date"
        )

    # Test s32 approved label of the form
    def test_s32_approved_label(self):
        form = ViewOldPurchasedRequestsForm()
        self.assertTrue(
            form.fields["s_32_approved"].label is None
            or form.fields["s_32_approved"].label == "S32 Approver approved"
        )

    # Test the purchase date label of the form
    def test_purchase_date_label(self):
        form = ViewOldPurchasedRequestsForm()
        self.assertTrue(
            form.fields["purchase_date"].label is None
            or form.fields["purchase_date"].label == "Purchase Date"
        )

    # Test the purchase amount label of the form
    def test_purchase_amount_label(self):
        form = ViewOldPurchasedRequestsForm()
        self.assertTrue(
            form.fields["purchase_amount"].label is None
            or form.fields["purchase_amount"].label == "Purchase Amount"
        )

    # Test the purchase method label of the form
    def test_purchase_method_label(self):
        form = ViewOldPurchasedRequestsForm()
        self.assertTrue(
            form.fields["purchase_method"].label is None
            or form.fields["purchase_method"].label == "Purchase Method"
        )

    # Test the confirmation number label of the form
    def test_confirmation_number_label(self):
        form = ViewOldPurchasedRequestsForm()
        self.assertTrue(
            form.fields["confirmation_number"].label is None
            or form.fields["confirmation_number"].label == "Confirmation Number"
        )

    # Test the purchase notes label of the form
    def test_purchase_notes_label(self):
        form = ViewOldPurchasedRequestsForm()
        self.assertTrue(
            form.fields["purchase_notes"].label is None
            or form.fields["purchase_notes"].label == "Purchase Notes"
        )


# Test class to test out the view old s32 approved requests form
class ViewOldS32ApprovedRequestsFormTest(TestCase):
    # Test the name label of the form
    def test_name_label(self):
        form = ViewOldS32ApprovedRequestsForm()
        self.assertTrue(
            form.fields["name"].label is None
            or form.fields["name"].label == "Name of Saas"
        )

    # Test the url label of the form
    def test_url_label(self):
        form = ViewOldS32ApprovedRequestsForm()
        self.assertTrue(
            form.fields["url"].label is None or form.fields["url"].label == "URL"
        )

    # Test the description label of the form
    def test_description_label(self):
        form = ViewOldS32ApprovedRequestsForm()
        self.assertTrue(
            form.fields["description"].label is None
            or form.fields["description"].label == "Description"
        )

    # Test the cost label of the form
    def test_cost_label(self):
        form = ViewOldS32ApprovedRequestsForm()
        self.assertTrue(
            form.fields["cost"].label is None or form.fields["cost"].label == "Cost"
        )

    # Test the currency label of the form
    def test_currency_label(self):
        form = ViewOldS32ApprovedRequestsForm()
        self.assertTrue(
            form.fields["currency"].label is None
            or form.fields["currency"].label == "Currency"
        )

    # Test the frequency label of the form
    def test_frequency_label(self):
        form = ViewOldS32ApprovedRequestsForm()
        self.assertTrue(
            form.fields["frequency"].label is None
            or form.fields["frequency"].label == "Frequency"
        )

    # Test units label of the form
    def test_units_label(self):
        form = ViewOldS32ApprovedRequestsForm()
        self.assertTrue(
            form.fields["units"].label is None or form.fields["units"].label == "Units"
        )

    # Test duration label of the form
    def test_duration_label(self):
        form = ViewOldS32ApprovedRequestsForm()
        self.assertTrue(
            form.fields["duration"].label is None
            or form.fields["duration"].label == "Duration"
        )

    # Test the comments label of the form
    def test_comments_label(self):
        form = ViewOldS32ApprovedRequestsForm()
        self.assertTrue(
            form.fields["comments"].label is None
            or form.fields["comments"].label == "Comments"
        )

    # Test the level of subscription label of the form
    def test_level_of_subscription_label(self):
        form = ViewOldS32ApprovedRequestsForm()
        self.assertTrue(
            form.fields["level_of_subscription"].label is None
            or form.fields["level_of_subscription"].label == "Level of Subscription"
        )

    # Test the number of users label of the form
    def test_number_of_users_label(self):
        form = ViewOldS32ApprovedRequestsForm()
        self.assertTrue(
            form.fields["number_of_users"].label is None
            or form.fields["number_of_users"].label == "Number of Users"
        )

    # Test the names of users label of the form
    def test_names_of_users_label(self):
        form = ViewOldS32ApprovedRequestsForm()
        self.assertTrue(
            form.fields["names_of_users"].label is None
            or form.fields["names_of_users"].label == "Names of Users"
        )

    # Test the account administrator label of the form
    def test_account_administrator_label(self):
        form = ViewOldS32ApprovedRequestsForm()
        self.assertTrue(
            form.fields["account_administrator"].label is None
            or form.fields["account_administrator"].label == "Account Administrator"
        )

    # Test the backup administrator label of the form
    def test_backup_administrator_label(self):
        form = ViewOldS32ApprovedRequestsForm()
        self.assertTrue(
            form.fields["backup_administrator"].label is None
            or form.fields["backup_administrator"].label == "Backup Administrator"
        )

    # Test the manager label of the form
    def test_manager_label(self):
        form = ViewOldS32ApprovedRequestsForm()
        self.assertTrue(
            form.fields["manager"].label is None
            or form.fields["manager"].label == "Manager"
        )

    # Test the manager label of the form
    def test_manager_reviewed_label(self):
        form = ViewOldS32ApprovedRequestsForm()
        self.assertTrue(
            form.fields["date_manager_reviewed"].label is None
            or form.fields["date_manager_reviewed"].label
            == "Date Manager reviewed the request"
        )

    # Test the manager approved label of the form
    def test_manager_approved_label(self):
        form = ViewOldS32ApprovedRequestsForm()
        self.assertTrue(
            form.fields["manager_approved"].label is None
            or form.fields["manager_approved"].label == "Manager Approved"
        )

    # Test the manager denied label of the form
    def test_manager_denied_label(self):
        form = ViewOldS32ApprovedRequestsForm()
        self.assertTrue(
            form.fields["manager_denied"].label is None
            or form.fields["manager_denied"].label == "Manager Denied"
        )

    # Test the submitted label of the form
    def test_submitted_by_label(self):
        form = ViewOldS32ApprovedRequestsForm()
        self.assertTrue(
            form.fields["submitted_by"].label is None
            or form.fields["submitted_by"].label == "Submitted By"
        )

    # Test the date info requested label of the form
    def test_date_info_requested_label(self):
        form = ViewOldS32ApprovedRequestsForm()
        self.assertTrue(
            form.fields["date_info_requested"].label is None
            or form.fields["date_info_requested"].label == "Date Info Requested"
        )

    # Test the info requested label of the form
    def test_info_requested_label(self):
        form = ViewOldS32ApprovedRequestsForm()
        self.assertTrue(
            form.fields["info_requested"].label is None
            or form.fields["info_requested"].label == "Info Requested"
        )

    # Test the fund center label of the form
    def test_fund_center_label(self):
        form = ViewOldS32ApprovedRequestsForm()
        self.assertTrue(
            form.fields["fund_center"].label is None
            or form.fields["fund_center"].label == "Fund Center"
        )

    # Test the approved by label of the form
    def test_approved_by_label(self):
        form = ViewOldS32ApprovedRequestsForm()
        self.assertTrue(
            form.fields["approved_by"].label is None
            or form.fields["approved_by"].label == "S32 Approver"
        )

    # Test the date sent to s32 approval label of the form
    def test_date_sent_to_s_32_approver_label(self):
        form = ViewOldS32ApprovedRequestsForm()
        self.assertTrue(
            form.fields["date_sent_to_s_32_approver"].label is None
            or form.fields["date_sent_to_s_32_approver"].label
            == "Date Sent to S32 Approver"
        )
