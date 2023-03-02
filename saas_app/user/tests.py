from django.test import TestCase
from .models import User, Users, Roles

# Unit tests to test the models and views of the saas_app application.

class UserTestCase(TestCase):
    # set up a model with the required fields
    def setUp(self):
        role = Roles.objects.create(name="Test Name", description="Test Description")
        auth_user = User.objects.create_user(username="Test User", password="Test Password")
        user = Users.objects.create(user=auth_user, first_name="Test First Name", last_name="Test Last Name", title="Test Title", business_unit="Test Business Unit")
        user.user_roles.add(role)
        
    # test that the model was created correctly
    # Test roles model
    def test_roles(self):
        roles = Roles.objects.get(name="Test Name")
        self.assertEqual(roles.description, "Test Description")
        
    # Test users model    
    def test_user(self):
        auth_user = User.objects.get(username="Test User")
        user = Users.objects.get(user=auth_user)
        self.assertEqual(user.user, auth_user)
        self.assertEqual(user.first_name, "Test First Name")
        self.assertEqual(user.last_name, "Test Last Name")
        self.assertEqual(user.user_roles.count(), 1)
        self.assertEqual(user.title, "Test Title")
        self.assertEqual(user.business_unit, "Test Business Unit")
