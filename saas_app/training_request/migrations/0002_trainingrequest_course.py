# Generated by Django 4.2.6 on 2023-11-07 17:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("training_request", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="trainingrequest",
            name="course",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="course",
                to="training_request.course",
                verbose_name="course",
            ),
            preserve_default=False,
        ),
    ]
