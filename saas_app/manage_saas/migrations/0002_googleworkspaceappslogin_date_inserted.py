# Generated by Django 4.2.3 on 2023-07-28 17:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("manage_saas", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="googleworkspaceappslogin",
            name="date_inserted",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
