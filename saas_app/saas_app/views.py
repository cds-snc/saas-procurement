from django.shortcuts import render
import django.contrib.messages as messages
from django.contrib.auth.signals import user_logged_in
from django.utils.translation import gettext as _
from submit_request.models import SaasRequest
from user.models import Users, Roles
from django.db.models import Q
import os


# Get the search term from the GET request and search the database for it
def search(request):
    if request.method == "GET":
        search_term = request.GET.get("search")
        try:
            # search for the search term in the name, description, status, url, and level of subscription fields
            results = SaasRequest.objects.filter(
                Q(name__icontains=search_term)
                | Q(description__icontains=search_term)
                | Q(status__icontains=search_term)
                | Q(url__icontains=search_term)
                | Q(level_of_subscription__icontains=search_term)
            )
        except Exception as e:
            print(e)
            messages.error(
                request, _("Something went wrong with the search. Please try again.")
            )
        return render(request, "search.html", {"results": results})
    else:
        return render(request, "search.html", {})


def view_request(request, pk):
    if request.method == "GET":
        # search for the request with the given primary key and display results
        saas_request = SaasRequest.objects.get(pk=pk)
        return render(request, "detail.html", {"saas_request": saas_request})


# Function to initialize the application and set the initial role to Requestor
def init(request):
    if request.method == "GET" and request.user.is_authenticated:
        # if we are testing then we need to add each user to each group for testing purposes
        if os.getenv("TESTING_FEATURE_FLAG"):
            user_logged_in.connect(create_groups)
            # Store the role in a session variable if it does not exist
            if request.session["role"] is None:
                request.session["role"] = "Requestor"
        return render(request, "index.html", {"role": request.session["role"]})
    else:
        # set initially that the role is requestor
        request.session["role"] = "Requestor"
        return render(request, "index.html", {})


# Function to switch to a new role
def switch_role(request):
    if request.method == "GET":
        try:
            # get the new role and set it in the session
            new_role = request.GET.get("role")
            request.session["role"] = new_role
            messages.success(
                request,
                _("You have successfully switched to the " + new_role + " role"),
            )
        except Exception:
            messages.error(
                request,
                _("Something went wrong with switching roles. Please try again."),
            )
        return render(request, "index.html", {"role": request.session["role"]})


def create_groups(sender, user, request, **kwargs):
    # if we are testing then we need to add each user to each group for testing purposes
    if os.getenv("TESTING_FEATURE_FLAG"):
        print("Adding user to groups")
        # if user does not exist, then create it and append every role to it
        results = Users.objects.filter(user__username=request.user.username)

        # If the user does not exist, meaning that this is the first time they are logging in, then create the user
        if results.count() == 0:
            user = Users(
                user=request.user,
                first_name=request.user.first_name,
                last_name=request.user.last_name,
            )
            user.save()
            roles = Roles.objects.all()
            user.user_roles.set(roles)
            user.save()
        else:
            print("User already exists")
