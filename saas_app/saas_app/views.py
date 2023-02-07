from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib import messages


class Home(TemplateView):
    template_name = "home.html"

def signup_redirect(request):
    messages.error(request, "Something wrong here, it may be that you already have account!")
    return redirect("home.html")

