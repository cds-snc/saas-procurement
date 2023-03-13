# Generated by Django 4.1.7 on 2023-03-13 21:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("submit_request", "0008_rename_approver_saasrequest_manager"),
    ]

    operations = [
        migrations.RenameField(
            model_name="saasrequest",
            old_name="date_reviewed",
            new_name="date_manager_reviewed",
        ),
        migrations.RenameField(
            model_name="saasrequest",
            old_name="approved",
            new_name="manager_approved",
        ),
        migrations.RenameField(
            model_name="saasrequest",
            old_name="denied",
            new_name="manager_denied",
        ),
    ]
