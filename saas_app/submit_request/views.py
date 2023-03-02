from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import SubmitRequestForm


def process_requets(request):
    if request.method == "POST":
        form = SubmitRequestForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            return render(request, "thanks.html")
    else:
        form = SubmitRequestForm()
    return render(request, "saas_request.html", {"form": form})
