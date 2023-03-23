from django.db import models
from django.utils.translation import gettext_lazy as _


# Model to store the fund center information
class FundCenter(models.Model):
    name = models.CharField(_("name"), max_length=100)
    number = models.CharField(_("number"), max_length=100)

    # return the string representation of the model
    def __str__(self):
        return self.name
