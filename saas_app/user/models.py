from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# Model to store the roles information
class Roles(models.Model):
    name = models.CharField(_("name"), max_length=100)
    description = models.CharField(_("description"), max_length=500)

    # return the string representation of the model
    def __str__(self):
        return self.name


# Model to store the users information
class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_roles = models.ManyToManyField(Roles)
    title = models.CharField(max_length=100)
    business_unit = models.CharField(max_length=100)

    # return the string representation of the model
    def __str__(self):
        return self.first_name + " " + self.last_name
