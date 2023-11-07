from django.db import models
from django.contrib.auth.models import User
from user.models import Users
from submit_request.models import Currency

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    provider = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    start_date = models.DateField()
    duration = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    cost = models.IntegerField()
    currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        null=True,
        default=None,
        blank=True,
    )
    

class TrainingRequest(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name="course", verbose_name="course"),
    fund_center = models.CharField(max_length=100)
    travel_living_costs = models.CharField(max_length=100)
    submitted_by = models.ForeignKey(
        User, on_delete=models.CASCADE 
    )
    status = models.CharField(max_length=100)
    manager = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name="manager",
        verbose_name="manager",
    )
    date_submitted = models.DateTimeField("date submitted", auto_now_add=True)
    date_manager_reviewed = models.DateTimeField(null=True, blank=True)
    s32_approved_by = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name="approved_by",
        null=True,
        blank=True,
    )
    date_s32_reviewed = models.DateTimeField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)

    # return the string representation of the Training request model
    def __str__(self):
        return self.course