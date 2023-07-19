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


# function to get the logs from Sentinel for the last day. Return the logs in a dataframe to display in the template as a table.
def get_sentinel_logs():
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
            print(error)
        elif response.status == LogsQueryStatus.SUCCESS:
            data = response.tables
            # represent the response in a pandas dataframe
            for table in data:
                df = pd.DataFrame(data=table.rows, columns=table.columns)
            return df
    except Exception as err:
        print("An error was encountered: ", err)


# function to view the logs in the Postgres DB
def view_logs(request):
    if request.method == "GET":
        logs = GoogleWorkspaceAppsLogin.objects.all()
        if logs is None:
            messages.error(
                request, _("Something went wrong and there are no logs to display!")
            )
        return render(request, "manage_saas/view_all_logs.html", {"all_logs": logs})


# function to schedule a daily crontab to retrieve data from sentinel and put it in the database for us
def daily_import_sentinel_data():
    print("Running daily import of Sentinel data")
    # get the logs from Sentinel
    logs = get_sentinel_logs()
    # for all the logs retrieved from Sentinel, save this in the Postgres database
    for log in logs.itertuples():
        logs = GoogleWorkspaceAppsLogin(
            time_generated=log.TimeGenerated,
            source_system=log.SourceSystem,
            kind=log.kind_s,
            application_name=log.app_name_s,
            user_email=log.actor_email_s,
            user_ip_address=log.IPAddress,
            event_name=log.event_name_s,
            client_id=log.client_id_s,
            application_name_id=log.id_applicationName_s,
            client_type=log.client_type_s,
            scope_data=log.scope_data_s,
            scope=log.scope_s,
            geolocation_country=log.geolocation_country_s,
            geolocation_city=log.geolocation_city_s,
            type=log.Type,
        )
        GoogleWorkspaceAppsLogin.save(logs)
