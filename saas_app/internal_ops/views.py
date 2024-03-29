from django.shortcuts import render, redirect
from django.utils.translation import get_language, gettext as _
from django.utils import timezone
from submit_request.models import SaasRequest
from user.models import Users
from .forms import (
    ViewS32RequestForm,
    ViewOldPurchasedRequestsForm,
    ViewOldS32ApprovedRequestsForm,
    ViewPurchaseRequiredForm,
)
import os
import django.contrib.messages as messages
import common.util.utils as utils
from approve.views import send_requestor_email
from django.views.decorators.csrf import csrf_exempt


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
        total_cost = cost * saas_object.units
        frequency = saas_object.frequency.frequency
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
                "total_cost": total_cost,
                "frequency": frequency,
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
            request, _("There was an error sending the email to the S32 approver.")
        )


def send_requestor_email_more_info(request, saas_object, info_requested, template_id):
    try:
        # get the requester's name, the saas_name, who submitted the request, the desciption, cost, subsciption level,
        # number of users, manager and the url
        saas_name = saas_object.name
        url = utils.get_current_site(request)
        submitted_by = (
            saas_object.submitted_by.first_name
            + " "
            + saas_object.submitted_by.last_name
        )
        submitted_by_email = saas_object.submitted_by.email
        internal_ops_name = (
            saas_object.internal_ops.user.first_name
            + " "
            + saas_object.internal_ops.user.last_name
        )
        internal_ops_email = saas_object.internal_ops.user.email
        info_requested = info_requested

        # send an email to the requestor
        utils.send_email(
            submitted_by_email,
            template_id,
            {
                "name": submitted_by,
                "saas_name": saas_name,
                "internal_ops_name": internal_ops_name,
                "internal_ops_email": internal_ops_email,
                "info_requested": info_requested,
                "url": url,
            },
        )
    except Exception as e:
        print(e)
        messages.error(
            request, _("There was an error sending the email to the requestor.")
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
    purchased_requests = SaasRequest.objects.filter(
        purchase_date__isnull=False, s_32_approved=True
    )

    return render(
        request,
        "internal_ops/view_all_requests.html",
        {
            "s32_approval_needed_requests": s32_approval_needed_requests,
            "purchase_needed_requests": purchase_needed_requests,
            "s32_approval_waiting_requests": s32_approval_waiting_requests,
            "purchased_requests": purchased_requests,
        },
    )


def view_all_prev_requests(request):
    s32_approval_waiting_requests = SaasRequest.objects.filter(
        s_32_review_date__isnull=True,
        manager_approved=True,
        date_sent_to_s_32_approver__isnull=False,
    )
    purchased_requests = SaasRequest.objects.filter(
        purchase_date__isnull=False, s_32_approved=True
    )

    return render(
        request,
        "internal_ops/view_all_prev_requests.html",
        {
            "s32_approval_waiting_requests": s32_approval_waiting_requests,
            "purchased_requests": purchased_requests,
        },
    )


def view_request(request, pk):
    if request.method == "GET":
        # search for the request with the given primary key
        saas_request = SaasRequest.objects.get(pk=pk)
        if saas_request.purchased is True:
            form = ViewOldPurchasedRequestsForm(instance=saas_request)
        elif (
            saas_request.s_32_review_date is None
            and saas_request.date_sent_to_s_32_approver is not None
        ):
            form = ViewOldS32ApprovedRequestsForm(instance=saas_request)
        elif (
            saas_request.s_32_review_date is not None
            and saas_request.s_32_approved is True
        ):
            form = ViewPurchaseRequiredForm(instance=saas_request)
        else:
            form = ViewS32RequestForm(instance=saas_request)
        return render(request, "internal_ops/view_request.html", {"form": form})
    elif request.method == "POST":
        saas_object = SaasRequest.objects.get(pk=pk)
        # initialize the instance to get teh id in the form
        form = ViewS32RequestForm(request.POST, instance=saas_object)
        # if the send for s32 approval button was clicked
        if request.POST.get("send_for_s32_approval"):
            # update the status
            try:
                if form.is_valid():
                    # update the fund center and the approved by fields
                    if (
                        form.cleaned_data["fund_center"] is not None
                        and form.cleaned_data["approved_by"] is not None
                    ):
                        saas_object.fund_center = form.cleaned_data["fund_center"]
                        saas_object.approved_by = form.cleaned_data["approved_by"]
                        saas_object.status = _("Waiting to be sent for S32 Approval")
                        saas_object.internal_ops = Users.objects.get(user=request.user)

                        try:
                            # Save the data to the database
                            saas_object = form.save()
                        except Exception as e:
                            print(e)
                            messages.error(
                                request,
                                _(
                                    "There was an error adding the fund center or the approver."
                                ),
                            )
                    else:
                        messages.error(
                            request, _("Please add the fund center and the approver.")
                        )
                        return render(
                            request, "internal_ops/view_request.html", {"form": form}
                        )

                saas_object.status = _("Sent to S32 Approver for Approval")
                saas_object.date_sent_to_s_32_approver = timezone.now()
                if saas_object.internal_ops is None:
                    saas_object.internal_ops = Users.objects.get(user=request.user)

                saas_object.save()
            except Exception as e:
                print(e)
                messages.error(
                    request, _("There was an error updating the status of the form.")
                )

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
                    request, _("We have successfully emailed the S32 approver.")
                )
            except Exception as e:
                print(e)
                messages.error(
                    request,
                    _(
                        "There was an error sending the notification emails to the S32 approver or requestor."
                    ),
                )
            return render(request, "internal_ops/view_request.html", {"form": form})


@csrf_exempt
def send_mail(request, pk):
    saas_object = SaasRequest.objects.get(pk=pk)
    current_language = get_language()
    if request.method == "POST" and request.POST.get("info_requested"):
        try:
            info_requested = request.POST.get("info_requested")
            if saas_object.internal_ops is None:
                saas_object.internal_ops = Users.objects.get(user=request.user)
            saas_object.status = _("Request for more information")
            saas_object.info_requested = info_requested
            saas_object.date_info_requested = timezone.now()
            saas_object.save()
            # send an email to the requestor
            send_requestor_email_more_info(
                request,
                saas_object,
                info_requested,
                os.getenv("INTERNAL_OPS_REQUEST_MORE_INFO_TEMPLATE_ID"),
            )
            messages.success(request, _("We have successfully emailed the requestor."))
        except Exception as e:
            print(e)
            messages.error(
                request,
                _(
                    "There was an error sending the notification email to the requestor."
                ),
            )
    else:
        messages.error(request, _("Please enter the information requested."))
    return redirect("/" + current_language + "/internal_ops/view/" + str(pk))


def purchase(request, pk):
    saas_object = SaasRequest.objects.get(pk=pk)
    current_language = get_language()
    if request.method == "POST":
        try:
            saas_object.purchase_date = request.POST.get("purchase-date")
            saas_object.purchase_method = request.POST.get("purchase-method")
            saas_object.purchase_amount = request.POST.get("purchase-amount")
            saas_object.confirmation_number = request.POST.get("confirmation-number")
            saas_object.purchase_notes = request.POST.get("purchase-notes")
            saas_object.status = _("Purchased")
            saas_object.purchased = True
            saas_object.save()
            messages.success(
                request, _("We have successfully recorded the purchase information")
            )
        except Exception as e:
            print(e)
            messages.error(
                request, _("There was an error recording the purchase information")
            )
    else:
        messages.error(request, _("Please enter the information requested."))
    return redirect("/" + current_language + "/internal_ops/view/" + str(pk))
