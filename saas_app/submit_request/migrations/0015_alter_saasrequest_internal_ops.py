# Generated by Django 4.1.7 on 2023-03-17 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0002_remove_users_roles_users_user_roles"),
        ("submit_request", "0014_saasrequest_internal_ops_alter_saasrequest_manager"),
    ]

    operations = [
        migrations.AlterField(
            model_name="saasrequest",
            name="internal_ops",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="internal_ops",
                to="user.users",
            ),
        ),
    ]
