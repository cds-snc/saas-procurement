# Generated by Django 4.2 on 2023-05-09 20:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("user", "0003_alter_roles_description_alter_roles_name"),
        ("submit_request", "0017_saasrequest_purchase_notes"),
    ]

    operations = [
        migrations.AddField(
            model_name="saasrequest",
            name="info_requested",
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name="saasrequest",
            name="account_administrator",
            field=models.CharField(
                max_length=100, verbose_name="account administrator"
            ),
        ),
        migrations.AlterField(
            model_name="saasrequest",
            name="backup_administrator",
            field=models.CharField(max_length=100, verbose_name="backup administrator"),
        ),
        migrations.AlterField(
            model_name="saasrequest",
            name="cost",
            field=models.CharField(max_length=100, verbose_name="cost"),
        ),
        migrations.AlterField(
            model_name="saasrequest",
            name="date_submitted",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="date submitted"
            ),
        ),
        migrations.AlterField(
            model_name="saasrequest",
            name="description",
            field=models.CharField(max_length=500, verbose_name="description"),
        ),
        migrations.AlterField(
            model_name="saasrequest",
            name="level_of_subscription",
            field=models.CharField(
                max_length=100, verbose_name="level of subscription"
            ),
        ),
        migrations.AlterField(
            model_name="saasrequest",
            name="manager",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="manager",
                to="user.users",
                verbose_name="manager",
            ),
        ),
        migrations.AlterField(
            model_name="saasrequest",
            name="name",
            field=models.CharField(max_length=100, verbose_name="name"),
        ),
        migrations.AlterField(
            model_name="saasrequest",
            name="names_of_users",
            field=models.CharField(max_length=500, verbose_name="names of users"),
        ),
        migrations.AlterField(
            model_name="saasrequest",
            name="number_of_users",
            field=models.IntegerField(verbose_name="number of users"),
        ),
        migrations.AlterField(
            model_name="saasrequest",
            name="submitted_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="submitted by",
            ),
        ),
    ]
