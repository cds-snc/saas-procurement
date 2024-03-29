from django.db import models
from django.contrib.auth.models import User
from user.models import Users
from internal_ops.models import FundCenter
from submit_request.models import Currency
from django.utils.html import format_html


# DB Model for the course
class Course(models.Model):
    course_title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
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

    # return the string representation of the Training request model
    def __str__(self):
        return self.course_title


# DB Model for a training request
class TrainingRequest(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="course",
        verbose_name="course",
    )
    fund_center = models.ForeignKey(
        FundCenter, on_delete=models.CASCADE, null=True, blank=True
    )
    travel_living_costs = models.CharField(max_length=100)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    manager = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name="training_manager",
        verbose_name="training_manager",
    )
    date_submitted = models.DateTimeField("date submitted", auto_now_add=True)
    date_manager_reviewed = models.DateTimeField(null=True, blank=True)
    s32_approved_by = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name="training_approved_by",
        null=True,
        blank=True,
    )
    date_s32_reviewed = models.DateTimeField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    pdf_form = models.FileField(upload_to="pdfs/", null=True, blank=True)
    within_budget = models.BooleanField(default=False)

    # return the string representation of the Training request model
    def __str__(self):
        return self.course.course_title

    def file_link(self):
        if self.pdf_form:
            return format_html("<a href='%s'>download</a>" % (self.pdf_form.url,))
        else:
            return "No attachment"

    file_link.allow_tags = True
