# Generated by Django 4.2.7 on 2023-11-27 23:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("training_request", "0005_trainingrequest_pdf_form"),
    ]

    operations = [
        migrations.RenameField(
            model_name="course",
            old_name="title",
            new_name="course_title",
        ),
    ]
