from django.db import models


# Model to store google workspace login information to third party apps
class GoogleWorkspaceAppsLogin(models.Model):
    time_generated = models.DateTimeField()
    source_system = models.CharField(max_length=100)
    kind = models.CharField(max_length=100)
    application_name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    user_ip_address = models.CharField(max_length=100)
    event_name = models.CharField(max_length=100)
    client_id = models.CharField(max_length=100)
    application_name_id = models.CharField(max_length=100)
    client_type = models.CharField(max_length=100)
    scope_data = models.CharField()
    scope = models.CharField()
    geolocation_country = models.CharField(max_length=100)
    geolocation_city = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    # return the string representation of the model
    def __str__(self):
        return self.application_name + " " + self.user_email
