# Generated by Django 4.1.7 on 2023-03-15 18:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "submit_request",
            "0009_rename_date_reviewed_saasrequest_date_manager_reviewed_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="saasrequest",
            name="date_sent_to_s_32_approver",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="saasrequest",
            name="purchase_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="saasrequest",
            name="purchased",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="saasrequest",
            name="s_32_approved",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="saasrequest",
            name="s_32_review_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
