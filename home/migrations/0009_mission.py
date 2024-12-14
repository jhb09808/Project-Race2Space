# Generated by Django 4.2.7 on 2024-11-17 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0008_newsarticle"),
    ]

    operations = [
        migrations.CreateModel(
            name="Mission",
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
                ("title", models.CharField(max_length=200)),
                ("summary", models.TextField()),
                ("link", models.URLField()),
                ("date", models.DateField()),
            ],
        ),
    ]