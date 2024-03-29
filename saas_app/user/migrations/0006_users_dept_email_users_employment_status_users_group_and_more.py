# Generated by Django 4.2.7 on 2023-11-15 01:09

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0005_users_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="users",
            name="dept_email",
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="users",
            name="employment_status",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="users",
            name="group",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="users",
            name="level",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="users",
            name="position",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="users",
            name="sector",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="users",
            name="telephone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True, max_length=128, null=True, region=None
            ),
        ),
    ]
