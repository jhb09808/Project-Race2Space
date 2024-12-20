# Generated by Django 4.2.7 on 2024-11-17 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_discussion_name_reply_name_alter_discussion_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="agencyprofile",
            name="latitude",
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="agencyprofile",
            name="longitude",
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]
