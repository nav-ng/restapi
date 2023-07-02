# Generated by Django 4.2 on 2023-05-03 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rest_app", "0007_bookmodel"),
    ]

    operations = [
        migrations.CreateModel(
            name="CompanyModel",
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
                ("ceo_name", models.CharField(max_length=50)),
                ("location", models.CharField(max_length=50)),
                ("opening_time", models.TimeField()),
                ("closing_time", models.TimeField()),
                ("address", models.TextField()),
                ("hr_name", models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(name="BookModel",),
    ]