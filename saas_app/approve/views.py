from django.shortcuts import render
import os
import common.util.utils as utils
from submit_request.models import SaasRequest, Users
from submit_request.views import send_requestor_email
from .forms import ViewRequestForm
import datetime

# Create your views here.

def view_all_requests(request):
    # get all the objects that need to be approved
    current_user = Users.objects.get(user=request.user)
    user_approval_needed_requests = SaasRequest.objects.filter(approver = current_user, date_reviewed = None)
    all_approval_needed_requests = SaasRequest.objects.filter(date_reviewed = None).exclude(approver=current_user)
    # render the requests in a table
    return render(
        request,
        "approve/view_all_requests.html",
        {"user_approval_needed_requests": user_approval_needed_requests,
         "all_approval_needed_requests": all_approval_needed_requests},
    )

    
def view_request(request, pk):
    if request.method == "GET":
        # search for the request with the given primary key
        saas_request = SaasRequest.objects.get(pk=pk)
        form = ViewRequestForm(instance=saas_request)
        return render(request, "approve/view_request.html", {"form": form})
    elif request.method == "POST":
        # if the save button was clicked
        if request.POST.get("approve"):
            # get the request object by its primary key
            saas_object = SaasRequest.objects.get(pk=pk)
            # update the approve field and notify the requestor
            saas_object.approved = True
            saas_object.date_reviewed = datetime.datetime.now()
            # Save the data to the database
            saas_object.save()
            # send emails to the requestor that an approval has been made
            send_requestor_email(
                request, saas_object, os.getenv("APPROVED_REQUEST_TEMPLATE_ID")
            )
            # redirect to a new URL
            return render(request, "approve/saas_status.html", {"status": "approved"})
        #else if the deny button was clicked
        elif request.POST.get("deny"):
            saas_object = SaasRequest.objects.get(pk=pk)
            # update the approve field and notify the requestor
            saas_object.denied = True
            saas_object.date_reviewed = datetime.datetime.now()
            # Save the data to the database
            saas_object.save()
            # send emails to the requestor that an approval has been made
            send_requestor_email(
                request, saas_object, os.getenv("DENIED_REQUEST_TEMPLATE_ID")
            )
            # redirect to a new URL
            return render(request, "approve/saas_status.html", {"status": "denied"})
        elif request.POST.get("request_info"):
            # TO DO: send an email to the requestor asking for more information 
            pass
