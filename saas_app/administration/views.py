from django.shortcuts import render
from django.utils.translation import gettext as _
from .forms import ViewUserForm
from user.models import Users
import django.contrib.messages as messages


# function to return the list of users. If POST request, then we update the user data
def view_users(request):
    if request.method == "GET":
        # search for all the users of the application 
        users = Users.objects.all()
        for user in users:
            user.roles = [role.name for role in user.user_roles.all()] 
        # render the requests in a table
        return render(
            request,
            "administration/view_all_users.html",
            {
                "all_users": users,
            },
        )


# function to view a single user and update the user data 
def view_user(request, pk):
    if request.method == "GET":
        # search for the user with the given primary key
        user = Users.objects.get(pk=pk)
        form = ViewUserForm(instance=user)
        return render(request, "administration/view_user.html", {"form": form})
    elif request.method == "POST":
        form = ViewUserForm(request.POST)
        # if the update button was clicked
        if request.POST.get("save"):
            if form.is_valid():
                # get the user object by its primary key
                user = Users.objects.get(pk=pk)
                # update all the fields
                user.first_name = form.cleaned_data["first_name"]
                user.last_name = form.cleaned_data["last_name"]
                #user.user_roles = form.cleaned_data["user_roles"]
                user.title = form.cleaned_data["title"]
                user.business_unit = form.cleaned_data["business_unit"]
                
                # save the user object
                try:
                    # Save the data to the database
                    user.save()
                    messages.success(request, _("The user data was updated successfully!"))
                except Exception:
                    messages.error(request, _("The user data was not saved successfully!"))
                
                return render(request, "administration/view_user.html", {"form": form})
        elif request.POST.get("update_roles"):
            if form.is_valid():
                # get the user object by its primary key
                user = Users.objects.get(pk=pk)
                # update the roles
                user.user_roles = form.cleaned_data["user_roles"]
                # save the user object
                try:
                    # Save the data to the database
                    user.save()
                    messages.success(request, _("The user's roles were updated successfully!"))
                except Exception:
                    messages.error(request, _("The user's roles were not updated successfully!"))
                
                return render(request, "administration/view_user.html", {"form": form})
            