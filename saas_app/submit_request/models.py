from django.db import models
from user.models import Users
from internal_ops.models import FundCenter
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


# Model to store the frequency of the request (values are daily, weekly, monthly, yearly, one time purchase)
class Frequency(models.Model):
    frequency = models.CharField(_("frequency"), max_length=100)
    description = models.CharField(_("description"), max_length=500)

    # return the string representation of the model
    def __str__(self):
        return self.frequency


# class to store the currency of the cost of the request (values include CDN, USD, EUR, etc.)
class Currency(models.Model):
    currency = models.CharField(_("currency"), max_length=10)
    description = models.CharField(_("description"), max_length=500)

    # return the string representation of the model
    def __str__(self):
        return self.currency


# Model to store the request information
class SaasRequest(models.Model):
    name = models.CharField(_("name"), max_length=100)
    url = models.URLField(max_length=100)
    description = models.CharField(_("description"), max_length=500)
    cost = models.CharField(_("cost"), max_length=100)
    currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        null=True,
        default="CDN",
        blank=True,
        related_name="saas_currency",
    )
    frequency = models.ForeignKey(
        Frequency,
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
        related_name="saas_frequency",
    )
    level_of_subscription = models.CharField(_("level of subscription"), max_length=100)
    units = models.IntegerField(_("units"))
    duration = models.CharField(_("duration"), max_length=100)
    number_of_users = models.IntegerField(_("number of users"))
    names_of_users = models.CharField(_("names of users"), max_length=500)
    account_administrator = models.CharField(_("account administrator"), max_length=100)
    backup_administrator = models.CharField(_("backup administrator"), max_length=100)
    manager = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name="manager",
        verbose_name=_("manager"),
    )
    submitted_by = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_("submitted by")
    )
    date_submitted = models.DateTimeField(_("date submitted"), auto_now_add=True)
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
    date_info_requested = models.DateTimeField(null=True, blank=True)
    info_requested = models.CharField(max_length=5000, null=True, blank=True)
    purchase_amount = models.FloatField(null=True, blank=True)
    purchase_method = models.CharField(max_length=100, null=True, blank=True)
    confirmation_number = models.CharField(max_length=100, null=True, blank=True)
    purchase_notes = models.CharField(max_length=500, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)

    # return the string representation of the model
    def __str__(self):
        return self.name
