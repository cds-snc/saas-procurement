from django.db import models


# Model to store the fund center information
class FundCenter(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)

    # return the string representation of the model
    def __str__(self):
        return self.name

