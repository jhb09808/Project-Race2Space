# Generated by Django 4.2.7 on 2024-11-23 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0011_timelineevent_media_caption_timelineevent_media_url"),
    ]

    operations = [
        migrations.CreateModel(
            name="SpaceObject",
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
                (
                    "international_designator",
                    models.CharField(blank=True, max_length=50),
                ),
                ("national_designator", models.CharField(blank=True, max_length=50)),
                ("name_of_space_object", models.CharField(max_length=100)),
                ("state_organization", models.CharField(max_length=100)),
                ("date_of_launch", models.DateField(blank=True, null=True)),
                ("gso_location", models.CharField(blank=True, max_length=100)),
                ("un_registered", models.CharField(blank=True, max_length=10)),
                ("registration_document", models.CharField(blank=True, max_length=100)),
                ("other_documents", models.TextField(blank=True)),
                ("status", models.CharField(blank=True, max_length=50)),
                ("date_of_decay_or_change", models.DateField(blank=True, null=True)),
                ("function_of_space_object", models.TextField(blank=True)),
                ("secretariats_remarks", models.TextField(blank=True)),
                ("external_website", models.URLField(blank=True)),
            ],
        ),
    ]