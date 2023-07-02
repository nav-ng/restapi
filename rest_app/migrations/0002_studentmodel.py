# Generated by Django 4.2 on 2023-04-18 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rest_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="StudentModel",
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
                ("student_id", models.IntegerField()),
                ("student_name", models.CharField(max_length=100)),
                ("student_address", models.CharField(max_length=100)),
            ],
        ),
    ]
