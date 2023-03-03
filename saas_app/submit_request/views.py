from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import SubmitRequestForm


def process_requets(request):
    if request.method == "POST":
        form = SubmitRequestForm(request.POST)
        if form.is_valid():
            # Save the data to the database
            saas_object = form.save(commit = False)
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
            approver_email = saas_object.approver.email
            # get the approver's name
            approver_name = saas_name.approver.first_name
            # get the url
            url = request.resolver_match.url_name

            # send an email to the requestor
            form.send_mail(requestor_email, os.getenv("SAAS_SUBMISSION_TEMPLATE_ID"), {"saas_name": saas_name, "name": request.user.first_name, "url": url})
            # send an email to the approver
            form.send_mail(approver_email, os.getenv("APPROVAL_REQUEST_TEMPLATE_ID"), {"saas_name": saas_name, "requestor": request.user.first_name, "name": approver_name, "url": url})

            # redirect to a new URL:
            return render(request, "thanks.html")
    else:
        form = SubmitRequestForm()
    return render(request, "saas_request.html", {"form": form})