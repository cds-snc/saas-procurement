# Generated by Django 4.2 on 2023-05-09 20:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0002_remove_users_roles_users_user_roles"),
    ]

    operations = [
        migrations.AlterField(
            model_name="roles",
            name="description",
            field=models.CharField(max_length=500, verbose_name="description"),
        ),
        migrations.AlterField(
            model_name="roles",
            name="name",
            field=models.CharField(max_length=100, verbose_name="name"),
        ),
    ]