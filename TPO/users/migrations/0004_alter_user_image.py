# Generated by Django 4.1 on 2022-12-14 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_user_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="image",
            field=models.ImageField(default="", upload_to="uploads/"),
        ),
    ]