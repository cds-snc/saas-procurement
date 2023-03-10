# Generated by Django 4.1.7 on 2023-03-01 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SaasRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("url", models.URLField(max_length=100)),
                ("description", models.CharField(max_length=500)),
                ("cost", models.CharField(max_length=100)),
                ("level_of_subscription", models.CharField(max_length=100)),
                ("number_of_users", models.IntegerField()),
                ("names_of_users", models.CharField(max_length=500)),
                ("account_administrator", models.CharField(max_length=100)),
                ("backup_administrator", models.CharField(max_length=100)),
                (
                    "approver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="user.users"
                    ),
                ),
            ],
        ),
    ]
