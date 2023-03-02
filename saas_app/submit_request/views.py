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
            # redirect to a new URL:
            return render(request, "thanks.html")
    else:
        form = SubmitRequestForm()
    return render(request, "saas_request.html", {"form": form})
