# Generated by Django 4.2.6 on 2023-11-09 17:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("training_request", "0004_alter_course_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="trainingrequest",
            name="pdf_form",
            field=models.FileField(blank=True, null=True, upload_to="pdfs/"),
        ),
    ]