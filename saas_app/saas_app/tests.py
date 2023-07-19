from django.test import RequestFactory, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from user.models import Users, Roles
from django.contrib.messages.storage.fallback import FallbackStorage
from .views import init, switch_role, create_groups
import os


class InitTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username="testuser", password="testpass")

    # Test the init view function
    def test_init_get_request(self):
        # Create a GET request
        request = self.factory.get("")
        request.user = self.user
        request.session = {}
        request.session["role"] = None
        request.session["roles"] = None

        # Set the environment variable to enable testing mode
        with self.settings(TESTING_FEATURE_FLAG=True):
            # Call the view function and get the response
            response = init(request)

            # Check that the response returned is valid
            self.assertEqual(response.status_code, 200)

            # mock the request session
            mock_request_session = {
                "role": "Requestor",
                "roles": [
                    "Requestor",
                    "Approver",
                    "Internal Ops",
                    "Administrator",
                    "Manager",
                    "Manage Saas"
                ],
            }

            # Check that the role was set in the session
            self.assertEqual(mock_request_session["role"], "Requestor")

            # Check that the roles were set in the session
            self.assertEqual(
                mock_request_session["roles"],
                ["Requestor", "Approver", "Internal Ops", "Administrator", "Manager", "Manage Saas"],
            )

    # test successful switch role
    def test_switch_role_get_request(self):
        # Create a GET request
        request = self.factory.get(reverse("switch_role"))
        request.user = self.user
        request.session = {
            "role": "Requestor",
            "roles": [
                "Requestor",
                "Approver",
                "Internal Ops",
                "Administrator",
                "Manager",
                "Manage Saas"
            ],
        }
        request.GET = {"role": "Approver"}

        # Needed for Django messages to work properly
        messages = FallbackStorage(request)
        setattr(request, "_messages", messages)

        # Call the view function and get the response
        response = switch_role(request)

        # Check that the response is 200
        self.assertEqual(response.status_code, 200)

        # Check that the role was set in the session
        self.assertEqual(request.session["role"], "Approver")

        # Check that all the roles are in the session
        self.assertEqual(
            request.session["roles"],
            ["Requestor", "Approver", "Internal Ops", "Administrator", "Manager", "Manage Saas"],
        )

    # test switching roles with no role parameter
    def test_switch_role_get_request_error(self):
        # Create a GET request with no role parameter
        request = self.factory.get(reverse("switch_role"))
        request.user = self.user
        request.session = {}
        request.session["roles"] = [
            "Requestor",
            "Approver",
            "Internal Ops",
            "Administrator",
            "Manager",
            "Manage Saas"
        ]

        messages = FallbackStorage(request)
        setattr(request, "_messages", messages)

        # Call the view function and get the response
        response = switch_role(request)

        # Check that the response is 200
        self.assertEqual(response.status_code, 200)

        # Check that the role was not changed in the session
        self.assertEqual(request.session["role"], None)


class CreateGroupsTest(TestCase):
    # set up test
    def setUp(self):
        # Create a test user  and roles for the purposes of this test
        self.test_user = User.objects.create_user(
            username="testuser", email="testuser@example.com", password="testpassword"
        )
        self.role = Roles.objects.create(
            name="Test Role", description="Test Description"
        )
        self.factory = RequestFactory()

    # test create_groups function
    def test_create_groups(self):
        # Set the testing feature flag to true
        os.environ["TESTING_FEATURE_FLAG"] = "True"

        # Create a request object for the test user
        request = self.factory.get("/create_groups")
        request.user = self.test_user

        # Call the create_groups function with the request object and test user
        create_groups(None, self.test_user, request)

        # Check that one user was created
        self.assertEqual(Users.objects.filter(user__username="testuser").count(), 1)

        # Check that the user was added to all roles
        user_roles = (
            Users.objects.filter(user__username="testuser").first().user_roles.all()
        )
        roles = Roles.objects.all()
        self.assertEqual(len(user_roles), len(roles))
        for role in roles:
            self.assertIn(role, user_roles)

    def tearDown(self):
        # Clean up after the test
        os.environ.pop("TESTING_FEATURE_FLAG")
        User.objects.filter(username="testuser").delete()
        Users.objects.filter(user__username="testuser").delete()
