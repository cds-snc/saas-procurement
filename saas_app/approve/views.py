from django.shortcuts import render
import django.contrib.messages as messages
import os
from submit_request.models import SaasRequest, Users
from submit_request.views import send_requestor_email
from .forms import ViewRequestForm
import datetime


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
                saas_object.status = "Manager approved"
                # Save the data to the database
                saas_object.save()
                # send emails to the requestor that an approval has been made
                send_requestor_email(
                    request, saas_object, os.getenv("APPROVED_REQUEST_TEMPLATE_ID")
                )
                messages.success(request, "Request has been successfully approved")
            except Exception as e:
                print(e)
                messages.error(request, "An error occurred while approving the request")
            # redirect to a new URL
            return render(request, "approve/saas_status.html", {"status": "approved"})
        # else if the deny button was clicked
        elif request.POST.get("deny"):
            try:
                saas_object = SaasRequest.objects.get(pk=pk)
                # update the approve field and notify the requestor
                saas_object.manager_denied = True
                saas_object.date_manager_reviewed = datetime.datetime.now()
                saas_object.status = "Manager denied"
                # Save the data to the database
                saas_object.save()
                # send emails to the requestor that an approval has been made
                send_requestor_email(
                    request, saas_object, os.getenv("DENIED_REQUEST_TEMPLATE_ID")
                )
                messages.success(request, "Request has been successfully denied")
            except Exception as e:
                print(e)
                messages.error(request, "An error occurred while denying the request")

            # redirect to a new URL
            return render(request, "approve/saas_status.html", {"status": "denied"})
        # elif request.POST.get("request_info"):
        #     print("request info")
        #     # TO DO: send an email to the requestor asking for more information
        #     return render(request, "approve/view_request.html", {"form": form})


# def send_email(request):
#     print("send email")
#     if request.method == "POST":
#         print("post")
#         pass
#     return render(request, "approve/view_request.html", {"form": form})

