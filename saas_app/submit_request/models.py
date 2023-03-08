from django.db import models
from user.models import Users
from django.contrib.auth.models import User


# Model to store the request information
class SaasRequest(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=100)
    description = models.CharField(max_length=500)
    cost = models.CharField(max_length=100)
    level_of_subscription = models.CharField(max_length=100)
    number_of_users = models.IntegerField()
    names_of_users = models.CharField(max_length=500)
    account_administrator = models.CharField(max_length=100)
    backup_administrator = models.CharField(max_length=100)
    approver = models.ForeignKey(Users, on_delete=models.CASCADE)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_submitted = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    # return the string representation of the model
    def __str__(self):
        return self.name
