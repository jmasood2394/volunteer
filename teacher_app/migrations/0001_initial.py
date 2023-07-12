# Generated by Django 4.2.1 on 2023-05-28 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("user_login", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Teacher",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("phone_number", models.CharField(max_length=10)),
                ("address", models.CharField(max_length=255)),
                (
                    "grade",
                    multiselectfield.db.fields.MultiSelectField(
                        choices=[
                            ("5th Grade", "5th Grade"),
                            ("6th Grade", "6th Grade"),
                            ("7th Grade", "7th Grade"),
                            ("8th Grade", "8th Grade"),
                            ("9th Grade", "9th Grade"),
                            ("10th Grade", "10th Grade"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "subjects",
                    multiselectfield.db.fields.MultiSelectField(
                        choices=[
                            ("English", "English"),
                            ("Math", "Math"),
                            ("Science", "Science"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "availability_days",
                    multiselectfield.db.fields.MultiSelectField(
                        choices=[
                            ("Monday", "Monday"),
                            ("Tuesday", "Tuesday"),
                            ("Wednesday", "Wednesday"),
                            ("Thursday", "Thursday"),
                            ("Friday", "Friday"),
                            ("Saturday", "Saturday"),
                            ("Sunday", "Sunday"),
                        ],
                        max_length=255,
                    ),
                ),
                ("availability_start", models.TimeField()),
                ("availability_end", models.TimeField()),
                (
                    "preferred_tutoring_format",
                    multiselectfield.db.fields.MultiSelectField(
                        choices=[("Online", "Online"), ("In Person", "In Person")],
                        max_length=255,
                    ),
                ),
                ("bio", models.TextField()),
            ],
        ),
    ]