# Generated by Django 4.2.7 on 2024-11-13 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AgencyProfile",
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
                ("country_name", models.CharField(max_length=100)),
                ("agency_name", models.CharField(max_length=100)),
                ("overview", models.TextField()),
                ("history", models.TextField()),
                ("notable_missions", models.TextField()),
                ("technological_innovations", models.TextField()),
                ("collaborations", models.TextField()),
                ("future_plans", models.TextField()),
            ],
        ),
    ]
