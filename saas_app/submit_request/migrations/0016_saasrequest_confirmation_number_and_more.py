# Generated by Django 4.1.7 on 2023-03-20 23:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("submit_request", "0015_alter_saasrequest_internal_ops"),
    ]

    operations = [
        migrations.AddField(
            model_name="saasrequest",
            name="confirmation_number",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="saasrequest",
            name="date_info_requested",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="saasrequest",
            name="purchase_method",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="saasrequest",
            name="purchse_amount",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
