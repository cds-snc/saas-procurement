from django.shortcuts import render
from .forms import SubmitRequestForm, ViewRequestForm
from .models import SaasRequest
import os
import common.util.utils as utils
import django.contrib.messages as messages



# Send an email to the requestor
def send_requestor_email(request, saas_object, template_id):
    # get the requester's email address
    requestor_email = request.user.email
    # get the requestors's name
    requestor_name = request.user.first_name
    # get the saas_name
    saas_name = saas_object.name
    # get the url
    url = utils.get_current_site(request)

    # send an email to the requestor
    utils.send_email(
        requestor_email,
        template_id,
        {"saas_name": saas_name, "name": requestor_name, "url": url},
    )


# send an email to the manager
def send_manager_email(request, saas_object, template_id):
    # get the requestors's name
    requestor_name = request.user.first_name
    # get the saas_name
    saas_name = saas_object.name
    # get the manager's email address
    manager_email = saas_object.manager.user.email
    # get the manager's name
    manager_name = saas_object.manager.user.first_name
    # get the url
    url = utils.get_current_site(request)

    # send an email to the manager
    utils.send_email(
        manager_email,
        template_id,
        {
            "saas_name": saas_name,
            "requestor": requestor_name,
            "name": manager_name,
            "url": url,
        },
    )


# Process the request form
def process_requests(request):
    if request.method == "POST":
        form = SubmitRequestForm(request.POST)
        if form.is_valid():
            # Save the data to the database
            saas_object = form.save(commit=False)
            # get the logged in user (ie the one submitting the request) and save it to the database
            saas_object.submitted_by = request.user
            saas_object.status = "Request submitted"
            saas_object.save()
            messages.info(request, "Your form was submitted successfully!")
            # send an email to the requestor and the manager
            send_requestor_email(
                request, saas_object, os.getenv("SAAS_SUBMISSION_TEMPLATE_ID")
            )

            # send an email to the manager
            send_manager_email(
                request, saas_object, os.getenv("APPROVAL_REQUEST_TEMPLATE_ID")
            )

            # redirect to a new URL:
            return render(request, "request/thanks.html")
    else:
        form = SubmitRequestForm()
    return render(request, "request/saas_request.html", {"form": form})


# function to return the list of submitted requests for the logged in user
def view_all_requests(request):
    if request.method == "GET":
        # search fro all the requests submitted by the logged in user
        submitted_requests = SaasRequest.objects.filter(
            submitted_by=request.user
        ).order_by("-date_manager_reviewed")
        # render the requests in a table
        return render(
            request,
            "request/view_all_requests.html",
            {"submitted_requests": submitted_requests},
        )


# function to view a single request and save or delete it
def view_request(request, pk):
    if request.method == "GET":
        # search for the request with the given primary key
        saas_request = SaasRequest.objects.get(pk=pk)
        form = ViewRequestForm(instance=saas_request)
        return render(request, "request/view_request.html", {"form": form})
    elif request.method == "POST":
        form = ViewRequestForm(request.POST)
        # if the save button was clicked
        if request.POST.get("save"):
            if form.is_valid():
                # get the request object by its primary key
                saas_object = SaasRequest.objects.get(pk=pk)
                # update all the fields
                saas_object.name = form.cleaned_data["name"]
                saas_object.url = form.cleaned_data["url"]
                saas_object.description = form.cleaned_data["description"]
                saas_object.cost = form.cleaned_data["cost"]
                saas_object.level_of_subscription = form.cleaned_data[
                    "level_of_subscription"
                ]
                saas_object.number_of_users = form.cleaned_data["number_of_users"]
                saas_object.names_of_users = form.cleaned_data["names_of_users"]
                saas_object.account_administrator = form.cleaned_data[
                    "account_administrator"
                ]
                saas_object.backup_administrator = form.cleaned_data[
                    "backup_administrator"
                ]
                saas_object.manager = form.cleaned_data["manager"]
                # Save the data to the database
                saas_object.save()
                # send emails to the requestor and manager that a change to the SaaS request has been made
                send_requestor_email(
                    request, saas_object, os.getenv("SAAS_SUBMISSION_EDIT_TEMPLATE_ID")
                )
                send_manager_email(
                    request, saas_object, os.getenv("EDIT_REQUEST_TEMPLATE_ID")
                )
                # redirect to a new URL:
                return render(request, "request/saas_edited.html")
        # else if the delete button was clicked
        elif request.POST.get("delete"):
            # obtain the saas object since we need to pass it for sending emails
            saas_object = SaasRequest.objects.get(pk=pk)
            # delete the saas request
            SaasRequest.objects.get(pk=pk).delete()
            # send an email to the requestor that the request has been deleted
            send_requestor_email(
                request, saas_object, os.getenv("DELETE_SAAS_REQUEST_TEMPLATE_ID")
            )
            send_manager_email(
                request, saas_object, os.getenv("APPROVER_DELETE_TEMPLATE_ID")
            )
            # redirect to a new URL:
            return render(request, "request/saas_deleted.html")
