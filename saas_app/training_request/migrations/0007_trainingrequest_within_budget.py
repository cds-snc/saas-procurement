# Generated by Django 4.2.7 on 2023-12-07 23:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("training_request", "0006_rename_title_course_course_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="trainingrequest",
            name="within_budget",
            field=models.BooleanField(default=False),
        ),
    ]