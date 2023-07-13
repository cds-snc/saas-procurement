from django.shortcuts import render
from django.utils.translation import gettext as _
from .forms import ViewUserForm
from user.models import Users, Roles
import django.contrib.messages as messages
from azure.identity import DefaultAzureCredential
from azure.monitor.query import LogsQueryClient, LogsQueryStatus
from datetime import datetime, timezone, timedelta
import os
import pandas as pd


# function to get the azure credentials and get a client to query the logs. Return the client to search for logs.
def azure_get_credentials():
    # get the client id 
    client_id = os.environ["AZURE_CLIENT_ID"]
    credentials = DefaultAzureCredential(managed_identity_client_id=client_id)
    logs_client = LogsQueryClient(credentials)
    return logs_client


# function to get the logs from Sentinel. Return the logs in a dataframe to display in the template as a table
def get_logs(request):
    
    # log into azure and get the logs client
    logs_client = azure_get_credentials()

    # query to get the logs from Sentinel, specifically the GWorkspace_ReportsAPI_token_CL table for the last 7 days
    query = """GWorkspace_ReportsAPI_token_CL"""
    start_date = datetime.now(tz=timezone.utc) - timedelta(days=7)
    end_date = datetime.now(tz=timezone.utc)

    try:
        # isssue the query to get the logs
        response = logs_client.query_workspace(
            workspace_id=os.environ["LOG_ANALYTICS_WORKSPACE_ID"],
            query=query,
            timespan=(start_date, end_date),
        )
        if response.status == LogsQueryStatus.PARTIAL:
            error = response.partial_error
            data = response.partial_data
            # generate an error if the query was not successful
            messages.error(
                request,
                _(
                    "There was an error retrieving the logs! The query did not execute fully and the results may be incomplete"
                ),
            )
            print(error)
        elif response.status == LogsQueryStatus.SUCCESS:
            data = response.tables
            # represent the response in a pandas dataframe
            for table in data:
                df = pd.DataFrame(data=table.rows, columns=table.columns)
            return df
    except Exception as err:
        print("An error was encountered: ", err)
        messages.error(
            request,
            _("There was an error retrieving the logs! The query was not successful!"),
        )


# function to view all the logs from Sentinel
def view_logs(request):
    if request.method == "GET":
        logs = get_logs(request)
        return render(request, "administration/view_all_logs.html", {"all_logs": logs})


# function to return the list of users. If POST request, then we update the user data
def view_users(request):
    if request.method == "GET":
        # search for all the users of the application
        users = Users.objects.all()
        for user in users:
            user.roles = ", ".join([role.name for role in user.user_roles.all()])
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
        get_logs(request)
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

                # get all the roles that exist in the database
                all_roles = Roles.objects.all()

                # remove all the roles from the user
                for role in all_roles:
                    user.user_roles.remove(role)

                # get all the roles from the form
                roles = form.cleaned_data["user_roles"]

                # add the roles from the form to the user
                for role in roles:
                    user.user_roles.add(role)

                request.session["roles"] = [role.name for role in roles]

                user.title = form.cleaned_data["title"]
                user.business_unit = form.cleaned_data["business_unit"]

                # save the user object
                try:
                    # Save the data to the database
                    user.save()
                    messages.success(
                        request, _("The user data was updated successfully!")
                    )
                except Exception:
                    messages.error(
                        request, _("The user data was not saved successfully!")
                    )

                return render(request, "administration/view_user.html", {"form": form})
