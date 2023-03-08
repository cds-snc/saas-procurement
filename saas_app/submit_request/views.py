from django.shortcuts import render
from .forms import SubmitRequestForm
from .models import SaasRequest
import os
import common.util.utils as utils


def process_requests(request):
    if request.method == "POST":
        form = SubmitRequestForm(request.POST)
        if form.is_valid():
            # Save the data to the database
            saas_object = form.save(commit=False)
            # get the logged in user (ie the one submitting the request) and save it to the database
            saas_object.submitted_by = request.user
            saas_object.save()

            # get the requester's email address
            requestor_email = request.user.email
            # get the requestors's name
            requestor_name = request.user.first_name
            # get the saas_name
            saas_name = saas_object.name
            # get thea approver's email address
            approver_email = saas_object.approver.user.email
            # get the approver's name
            approver_name = saas_object.approver.user.first_name
            # get the url
            url = utils.get_current_site(request)

            # send an email to the requestor
            utils.send_email(
                requestor_email,
                os.getenv("SAAS_SUBMISSION_TEMPLATE_ID"),
                {"saas_name": saas_name, "name": requestor_name, "url": url},
            )

            # send an email to the approver
            utils.send_email(
                approver_email,
                os.getenv("APPROVAL_REQUEST_TEMPLATE_ID"),
                {
                    "saas_name": saas_name,
                    "requestor": requestor_name,
                    "name": approver_name,
                    "url": url,
                },
            )

            # redirect to a new URL:
            return render(request, "thanks.html")
    else:
        form = SubmitRequestForm()
    return render(request, "saas_request.html", {"form": form})


# function to return the list of submitted requests for the logged in user
def view_request(request):
    if request.method == "GET":
        # search fro all the requests submitted by the logged in user
        submitted_requests = SaasRequest.objects.filter(submitted_by=request.user)
        # render the requests in a table
        return render(
            request, "view_request.html", {"submitted_requests": submitted_requests}
        )
