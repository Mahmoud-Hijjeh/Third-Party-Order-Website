# Generated by Django 4.1 on 2022-12-29 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_alter_user_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="delivery",
            name="account_name",
            field=models.CharField(default=" Account name ", max_length=50),
        ),
        migrations.AddField(
            model_name="store",
            name="account_name",
            field=models.CharField(default=" Account name ", max_length=50),
        ),
    ]