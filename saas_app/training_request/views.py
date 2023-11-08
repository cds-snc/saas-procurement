from django.shortcuts import render
from django.utils.translation import gettext as _
from .forms import TrainingForm, CourseForm
from .models import TrainingRequest
import django.contrib.messages as messages


# Process the request form
def process_requests(request):
    if request.method == "POST":
        course_form = CourseForm(request.POST)
        form = TrainingForm(request.POST)
        if form.is_valid() and course_form.is_valid():
            # Save the data to the database
            course_object = course_form.save(commit=False)
            course_object.save()
            training_object = form.save(commit=False)
            training_object.submitted_by = request.user
            # Save the course object to the training object
            training_object.course = course_object
            training_object.status = _("Request submitted")
            training_object.save()
            messages.success(
                request, _("Your training form was submitted successfully!")
            )

            # redirect to a new URL:
            return render(request, "request/training_thanks.html")
    else:
        # Clear the forms so that we can display them
        form = TrainingForm()
        course_form = CourseForm()

    return render(
        request,
        "training/training_request.html",
        {"form": form, "course_form": course_form},
    )


# function to return the list of submitted training requests for the logged in user
def view_all_requests(request):
    if request.method == "GET":
        # search for all the training requests submitted by the logged in user
        submitted_training_requests = TrainingRequest.objects.filter(
            submitted_by=request.user, date_manager_reviewed__isnull=True
        )
        prev_submitted_training_requests = TrainingRequest.objects.filter(
            submitted_by=request.user, date_manager_reviewed__isnull=False
        ).order_by("-date_manager_reviewed")
        # render the requests in a table
        return render(
            request,
            "training/view_all_requests.html",
            {
                "submitted_requests": submitted_training_requests,
                "prev_submitted_requests": prev_submitted_training_requests,
            },
        )


# function to view a single training request
def view_request(request, pk):
    if request.method == "GET":
        # search for the request with the given primary key
        training_request = TrainingRequest.objects.get(pk=pk)
        course_form = CourseForm(instance=training_request.course)
        form = TrainingForm(instance=training_request)
        return render(
            request,
            "training/view_request.html",
            {"form": form, "course_form": course_form},
        )
