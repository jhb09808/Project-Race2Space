# Generated by Django 4.2.7 on 2024-11-13 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="agencyprofile",
            name="flag",
            field=models.ImageField(default="", upload_to="flags/"),
            preserve_default=False,
        ),
    ]