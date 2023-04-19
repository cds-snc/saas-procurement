from django.shortcuts import render
import django.contrib.messages as messages
import os
from submit_request.models import SaasRequest, Users
from .forms import ViewRequestForm
import datetime
import common.util.utils as utils
from django.utils.translation import gettext as _


def send_requestor_email(request, saas_object, template_id):
    # get the requester's email address
    requestor_email = saas_object.submitted_by.email
    # get the requestors's name
    requestor_name = saas_object.submitted_by.first_name
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


def send_internal_ops_email(request, saas_object, template_id):
    # get the internal ops's email address
    internal_ops_email = saas_object.internal_ops.user.email
    # get the requestors's name
    requestor = (
        saas_object.submitted_by.first_name + " " + saas_object.submitted_by.last_name
    )
    # get the internal ops name
    internal_ops_name = request.user.first_name + " " + request.user.last_name
    # get the s32 approver
    s_32_approver = (
        saas_object.approved_by.user.first_name
        + " "
        + saas_object.approved_by.user.last_name
    )
    # get the saas_name
    saas_name = saas_object.name
    # get the url
    url = utils.get_current_site(request)

    # send an email to the requestor
    utils.send_email(
        internal_ops_email,
        template_id,
        {
            "saas_name": saas_name,
            "name": internal_ops_name,
            "requestor": requestor,
            "s32_approver": s_32_approver,
            "url": url,
        },
    )


def view_all_requests(request):
    # get all the objects that need to be approved
    try:
        current_user = Users.objects.get(user=request.user)
    except Exception:
        current_user = None

    user_approval_needed_requests = SaasRequest.objects.filter(
        manager=current_user, date_manager_reviewed=None
    )
    all_old_requests = SaasRequest.objects.filter(manager=current_user).exclude(
        date_manager_reviewed=None
    )

    # render the requests in a table
    return render(
        request,
        "approve/view_all_requests.html",
        {
            "user_approval_needed_requests": user_approval_needed_requests,
            "all_approval_needed_requests": all_old_requests,
        },
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
            try:
                # get the request object by its primary key
                saas_object = SaasRequest.objects.get(pk=pk)
                # update the approve field and notify the requestor
                saas_object.manager_approved = True
                saas_object.date_manager_reviewed = datetime.datetime.now()
                saas_object.status = _("Manager approved")
                # Save the data to the database
                saas_object.save()
                # send emails to the requestor that an approval has been made
                send_requestor_email(
                    request, saas_object, os.getenv("APPROVED_REQUEST_TEMPLATE_ID")
                )
                messages.success(request, _("Request has been successfully approved"))
            except Exception as e:
                print(e)
                messages.error(
                    request, _("An error occurred while approving the request")
                )
            # redirect to a new URL
            return render(request, "approve/saas_status.html", {"status": "approved"})
        # else if the deny button was clicked
        elif request.POST.get("deny"):
            try:
                saas_object = SaasRequest.objects.get(pk=pk)
                # update the approve field and notify the requestor
                saas_object.manager_denied = True
                saas_object.date_manager_reviewed = datetime.datetime.now()
                saas_object.status = _("Manager denied")
                # Save the data to the database
                saas_object.save()
                # send emails to the requestor that an approval has been made
                send_requestor_email(
                    request, saas_object, os.getenv("DENIED_REQUEST_TEMPLATE_ID")
                )
                messages.success(request, _("Request has been successfully denied"))
            except Exception as e:
                print(e)
                messages.error(
                    request, _("An error occurred while denying the request")
                )

            # redirect to a new URL
            return render(request, "approve/saas_status.html", {"status": "denied"})
        elif request.POST.get("request_info"):
            # TO DO: send an email to the requestor asking for more information
            pass


def view_all_requests_s32_approver(request):
    # get all the objects that need to be approved
    try:
        current_user = Users.objects.get(user=request.user)
    except Exception:
        current_user = None

    s32_approval_needed_requests = SaasRequest.objects.filter(
        approved_by=current_user,
        s_32_review_date=None,
        date_sent_to_s_32_approver__isnull=False,
    )
    all_old_requests = SaasRequest.objects.filter(approved_by=current_user).exclude(
        s_32_review_date=None
    )

    # render the requests in a table
    return render(
        request,
        "approve/view_all_requests.html",
        {
            "user_approval_needed_requests": s32_approval_needed_requests,
            "all_approval_needed_requests": all_old_requests,
        },
    )


def view_request_s32_approver(request, pk):
    if request.method == "GET":
        # search for the request with the given primary key
        saas_request = SaasRequest.objects.get(pk=pk)
        form = ViewRequestForm(instance=saas_request)
        return render(request, "approve/view_request.html", {"form": form})
    elif request.method == "POST":
        # if the save button was clicked
        if request.POST.get("approve"):
            try:
                # get the request object by its primary key
                saas_object = SaasRequest.objects.get(pk=pk)
                # update the approve field and notify the requestor
                saas_object.s_32_approved = True
                saas_object.s_32_review_date = datetime.datetime.now()
                saas_object.status = _("S32 approved")
                # Save the data to the database
                saas_object.save()
                # send emails to the requestor that an approval has been made
                send_requestor_email(
                    request, saas_object, os.getenv("REQUEST_S32_APPROVED_TEMPLATE_ID")
                )
                # send internal ops an email that the request has been approved
                send_internal_ops_email(
                    request,
                    saas_object,
                    os.getenv("REQUEST_S32_APPROVED_INTERNAL_OPS_TEMPLATE_ID"),
                )
                messages.success(request, _("Request has been successfully approved"))
            except Exception as e:
                print(e)
                messages.error(
                    request, _("An error occurred while approving the request")
                )
            # redirect to a new URL
            return render(request, "approve/saas_status.html", {"status": "approved"})
        # else if the deny button was clicked
        elif request.POST.get("deny"):
            try:
                saas_object = SaasRequest.objects.get(pk=pk)
                # update the approve field and notify the requestor
                saas_object.s_32_approved = False
                saas_object.s_32_review_date = datetime.datetime.now()
                saas_object.status = _("S32 denied")
                # Save the data to the database
                saas_object.save()
                # send emails to the requestor that an approval has been made
                send_requestor_email(
                    request, saas_object, os.getenv("REQUEST_S32_DENIED_TEMPLATE_ID")
                )
                # send internal ops email to notify that a request has been denied
                send_internal_ops_email(
                    request,
                    saas_object,
                    os.getenv("REQUEST_S32_DENIED_INTERNAL_OPS_TEMPLATE_ID"),
                )
                messages.success(request, _("Request has been successfully denied"))
            except Exception as e:
                print(e)
                messages.error(
                    request, _("An error occurred while denying the request")
                )

            # redirect to a new URL
            return render(request, "approve/saas_status.html", {"status": "denied"})
