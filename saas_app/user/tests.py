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
        
    # Test the lengths of the fields in the Role model
    def test_roles_field_max_lengths(self):
        roles = Roles.objects.get(name="Test Name")
        self.assertEqual(roles._meta.get_field('name').max_length, 100)
        self.assertEqual(roles._meta.get_field('description').max_length, 500)
    
    # Test that the string representation of the Role model is correctly returned
    def test_roles_string_representation(self):
        roles = Roles.objects.get(name="Test Name")
        self.assertEqual(str(roles), "Test Name")
        
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

    # Test the lengths of the fields in the models
    def test_user_field_max_lengths(self):
        user = Users.objects.get(first_name="Test First Name")
        self.assertEqual(user._meta.get_field('first_name').max_length, 100)
        self.assertEqual(user._meta.get_field('last_name').max_length, 100)
        self.assertEqual(user._meta.get_field('title').max_length, 100)
        self.assertEqual(user._meta.get_field('business_unit').max_length, 100)
        
    # Test that the string representation of the User model is correctly returned
    def test_user_string_representation(self):
        user = Users.objects.get(first_name="Test First Name")
        self.assertEqual(str(user), "Test First Name Test Last Name")