from django.db import models
from user.models import Users
from internal_ops.models import FundCenter
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
    manager = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="manager")
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_submitted = models.DateTimeField(auto_now_add=True)
    approved_by = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name="approved_by",
        null=True,
        blank=True,
    )
    date_manager_reviewed = models.DateTimeField(null=True, blank=True)
    manager_approved = models.BooleanField(default=False)
    manager_denied = models.BooleanField(default=False)
    s_32_approved = models.BooleanField(default=False)
    s_32_review_date = models.DateTimeField(null=True, blank=True)
    internal_ops = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name="internal_ops",
        null=True,
        blank=True,
    )
    date_sent_to_s_32_approver = models.DateTimeField(null=True, blank=True)
    purchase_date = models.DateTimeField(null=True, blank=True)
    purchased = models.BooleanField(default=False)
    fund_center = models.ForeignKey(
        FundCenter, on_delete=models.CASCADE, null=True, blank=True
    )
    status = models.CharField(max_length=100, null=True, blank=True)

    # return the string representation of the model
    def __str__(self):
        return self.name
