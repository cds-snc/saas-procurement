# Generated by Django 4.1.7 on 2023-03-10 03:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("submit_request", "0004_saasrequest_date_reviewed_saasrequest_denied"),
    ]

    operations = [
        migrations.AddField(
            model_name="saasrequest",
            name="approved_by",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="approved_by",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
