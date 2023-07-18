from django.shortcuts import render
from django.utils.translation import gettext as _
from .models import GoogleWorkspaceAppsLogin
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
    start_date = datetime.now(tz=timezone.utc) - timedelta(days=1)
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
        return render(request, "manage_saas/view_all_logs.html", {"all_logs": logs})

# function to schedule a daily crontab to retrieve data from sentinel and put it in the database for us
def daily_import_sentinel_data():
    logs = get_logs()
    for log in logs.itertuples():
        logs = GoogleWorkspaceAppsLogin(
            time_generated=log.TimeGenerated,
            source_system=log.SourceSystem,
            kind=log.Kind,
            application_name=log.ApplicationName,
            user_email=log.UserEmail,
            user_ip_address=log.UserIPAddress,
            event_name=log.EventName,
            client_id=log.ClientId,
            application_name_id=log.ApplicationNameId,
            client_type=log.ClientType,
            scope_data=log.ScopeData,
            scope=log.Scope,
            geolocation_country=log.GeolocationCountry,
            geolocation_city=log.GeolocationCity,
            type=log.Type,
        )