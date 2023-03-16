from django.shortcuts import render, redirect
from submit_request.models import SaasRequest
from .forms import ViewS32RequestForm
import datetime
import os
import django.contrib.messages as messages
import common.util.utils as utils
from submit_request.views import send_requestor_email

# Send an email to the requestor
def send_s32_approval_email(request, saas_object, template_id):
    # get the requester's email address, name, the saas_name, who submitted the request, the desciption, cost, subsciption level,
    # number of users, manager and the url
    requestor_email = request.user.email
    requestor_name = request.user.first_name
    saas_name = saas_object.name
    url = utils.get_current_site(request)
    submitted_by = saas_object.submitted_by
    s32_approver = saas_object.s_32_approver
    cost = saas_object.cost
    description = saas_object.description
    subsciption_level = saas_object.subsciption_level
    number_of_users = saas_object.number_of_users
    manager = saas_object.manager
    s32_approver_email = saas_object.s_32_approver.user.email

    # send an email to the s32 approver
    utils.send_email(
        s32_approver_email,
        template_id,
        {"saas_name": saas_name, "name": s32_approver, "cost": cost, "description": description, "submitted_by" :submitted_by, "subscription_level": subsciption_level, "number_of_users": number_of_users, "manager": manager, "url": url},
    )

def view_all_requests(request):
    s32_approval_needed_requests = SaasRequest.objects.filter(s_32_review_date=None, manager_approved=True).exclude(date_manager_reviewed=None)
    purchase_needed_requests = SaasRequest.objects.filter(purchase_date = None, s_32_approved=True ).exclude(s_32_review_date=None, date_manager_reviewed=None)
   
    # render the requests in a table
    return render(
        request,
        "internal_ops/view_all_requests.html",
        {
            "s32_approval_needed_requests": s32_approval_needed_requests,
            "purchase_needed_requests": purchase_needed_requests,
        },
    )


def view_request(request, pk):
    if request.method == "GET":
        # search for the request with the given primary key
        saas_request = SaasRequest.objects.get(pk=pk)
        form = ViewS32RequestForm(instance=saas_request)
        return render(request, "approve/view_request.html", {"form": form})
    elif request.method == "POST":
        form = ViewS32RequestForm(request.POST)
        # if the save button was clicked
        if request.POST.get("save"):
            saas_object = SaasRequest.objects.get(pk=pk)
            if form.is_valid():
                # saas_object = SaasRequest.objects.get(pk=pk)
                # update the fund center and the approved by fields
                if (form.cleaned_data["fund_center"] != None and form.cleaned_data["approved_by"] != None):
                    saas_object.fund_center = form.cleaned_data["fund_center"]
                    saas_object.approved_by = form.cleaned_data["approved_by"]
                    saas_object.date_sent_to_s_32_approver = datetime.datetime.now()
                    saas_object.status = "Waiting to be sent for S32 Approval"
                    # Save the data to the database
                    saas_object.save()
                    messages.success(request, "The form was successfully saved.")
                else:
                    messages.error(request, "Please add the fund center and the approver.")
            return render(request, "internal_ops/view_request.html", {"form": form})
        elif request.POST.get("send_for_s32_approval"):
            # Email the S32 approver to review the form and the requestor that the form has been sent for s32 approval
            # email to requestor notifying them that the requst is under s32 review
            send_requestor_email(
                request, saas_object, os.getenv("REQUESTOR_S32APPROVAL_PENDING_REVIEW_TEMPLATE_ID")
            )
            # send an email to the s32 approver
            send_s32_approval_email(request, saas_object, os.getenv("S32_APPROVAL_REQUESTED_TEMPLATE_ID"))


            # send an email to the requestor and the manager
            # send_requestor_email(
            #     request, saas_object, os.getenv("SAAS_SUBMISSION_TEMPLATE_ID")
            # )
            # redirect to a new URL:
            #return render(request, "request/thanks.html")
        # else if the deny button was clicked
        # elif request.POST.get("deny"):
        #     saas_object = SaasRequest.objects.get(pk=pk)
        #     # update the approve field and notify the requestor
        #     saas_object.manager_denied = True
        #     saas_object.date_manager_reviewed = datetime.datetime.now()
        #     # Save the data to the database
        #     saas_object.save()
        #     # send emails to the requestor that an approval has been made
        #     send_requestor_email(
        #         request, saas_object, os.getenv("DENIED_REQUEST_TEMPLATE_ID")
        #     )
        #     # redirect to a new URL
        #     return render(request, "approve/saas_status.html", {"status": "denied"})
        # elif request.POST.get("request_info"):
        #     # TO DO: send an email to the requestor asking for more information
        #     pass

