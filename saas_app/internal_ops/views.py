from django.shortcuts import render
from django.utils import timezone
from submit_request.models import SaasRequest
from user.models import Users
from .forms import ViewS32RequestForm
import os
import django.contrib.messages as messages
import common.util.utils as utils
from submit_request.views import send_requestor_email


# Send an email to the requestor
def send_s32_approval_email(request, saas_object, template_id):
    try:
        # get the requester's email address, name, the saas_name, who submitted the request, the desciption, cost, subsciption level,
        # number of users, manager and the url
        requestor_name = request.user.first_name + " " + request.user.last_name
        saas_name = saas_object.name
        url = utils.get_current_site(request)
        submitted_by = (
            saas_object.submitted_by.first_name
            + " "
            + saas_object.submitted_by.last_name
        )
        s32_approver = (
            saas_object.approved_by.user.first_name
            + " "
            + saas_object.approved_by.user.last_name
        )
        cost = saas_object.cost
        description = saas_object.description
        subsciption_level = saas_object.level_of_subscription
        number_of_users = saas_object.number_of_users
        manager = (
            saas_object.manager.user.first_name
            + " "
            + saas_object.manager.user.last_name
        )
        s32_approver_email = saas_object.approved_by.user.email
        # send an email to the s32 approver
        utils.send_email(
            s32_approver_email,
            template_id,
            {
                "name": s32_approver,
                "saas_name": saas_name,
                "cost": cost,
                "total_cost": cost,
                "description": description,
                "requestor": requestor_name,
                "submitted_by": submitted_by,
                "subscription_level": subsciption_level,
                "number_of_users": number_of_users,
                "manager": manager,
                "url": url,
            },
        )
    except Exception as e:
        print(e)
        messages.error(
            request, "There was an error sending the email to the S32 approver."
        )


def view_all_requests(request):
    s32_approval_needed_requests = SaasRequest.objects.filter(
        date_sent_to_s_32_approver=None, manager_approved=True
    ).exclude(date_manager_reviewed=None)
    purchase_needed_requests = SaasRequest.objects.filter(
        purchase_date=None, s_32_approved=True
    ).exclude(s_32_review_date=None, date_manager_reviewed=None)
    s32_approval_waiting_requests = SaasRequest.objects.filter(
        s_32_review_date__isnull=True,
        manager_approved=True,
        date_sent_to_s_32_approver__isnull=False,
    )

    return render(
        request,
        "internal_ops/view_all_requests.html",
        {
            "s32_approval_needed_requests": s32_approval_needed_requests,
            "purchase_needed_requests": purchase_needed_requests,
            "s32_approval_waiting_requests": s32_approval_waiting_requests,
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
        saas_object = SaasRequest.objects.get(pk=pk)
        # if the save button was clicked
        if request.POST.get("save"):
            if form.is_valid():
                # update the fund center and the approved by fields
                if (
                    form.cleaned_data["fund_center"] is not None
                    and form.cleaned_data["approved_by"] is not None
                ):
                    saas_object.fund_center = form.cleaned_data["fund_center"]
                    saas_object.approved_by = form.cleaned_data["approved_by"]
                    saas_object.date_sent_to_s_32_approver = timezone.now()
                    saas_object.status = "Waiting to be sent for S32 Approval"
                    saas_object.internal_ops = Users.objects.get(user=request.user)

                    try:
                        # Save the data to the database
                        saas_object.save()
                        messages.success(request, "The form was successfully saved.")
                    except Exception as e:
                        print(e)
                        messages.error(request, "There was an error saving the form.")
                else:
                    messages.error(
                        request, "Please add the fund center and the approver."
                    )
            return render(request, "internal_ops/view_request.html", {"form": form})
        elif request.POST.get("send_for_s32_approval"):
            # update the status
            try:
                saas_object.status = "Sent to S32 Approver for Approval"
                saas_object.date_sent_to_s_32_approver = timezone.now()
                saas_object.save()
            except Exception as e:
                print(e)
                messages.error(
                    request, "There was an error updating the status of the form."
                )

            # if the approver or fund center is not set, then return an error
            if saas_object.fund_center is None or saas_object.approved_by is None:
                messages.error(
                    request,
                    "Please add the fund center and the approver and then save the form.",
                )
                return render(request, "internal_ops/view_request.html", {"form": form})

            # Email the S32 approver to review the form and the requestor that the form has been sent for s32 approval
            try:
                send_requestor_email(
                    request,
                    saas_object,
                    os.getenv("REQUESTOR_S32APPROVAL_PENDING_REVIEW_TEMPLATE_ID"),
                )
                # send an email to the s32 approver
                send_s32_approval_email(
                    request,
                    saas_object,
                    os.getenv("S32_APPROVAL_REQUESTED_TEMPLATE_ID"),
                )
                messages.success(
                    request, "We have successfully emailed the S32 approver."
                )
            except Exception as e:
                print(e)
                messages.error(
                    request,
                    "There was an error sending the notification emails to the S32 approver or requestor.",
                )
            return render(request, "internal_ops/view_request.html", {"form": form})
