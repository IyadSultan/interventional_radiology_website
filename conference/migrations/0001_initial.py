# Generated by Django 5.0.2 on 2025-03-16 20:44

import conference.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Registration",
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
                ("full_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(blank=True, max_length=20, null=True)),
                ("institution", models.CharField(max_length=200)),
                (
                    "attendee_type",
                    models.CharField(
                        choices=[
                            ("specialist", "Specialist"),
                            ("trainee", "Trainee/Fellow"),
                        ],
                        max_length=20,
                    ),
                ),
                ("special_requirements", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Session",
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
                ("name", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True, null=True)),
                ("date", models.DateField()),
                ("start_time", models.TimeField()),
                ("end_time", models.TimeField()),
            ],
            options={
                "ordering": ["date", "start_time"],
            },
        ),
        migrations.CreateModel(
            name="Speaker",
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
                ("name", models.CharField(max_length=100)),
                ("title", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "institution",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("bio", models.TextField()),
                (
                    "photo",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=conference.models.get_unique_filename,
                    ),
                ),
                (
                    "order",
                    models.IntegerField(
                        default=0, help_text="Display order on the speakers page"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ScheduleItem",
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
                ("description", models.TextField(blank=True, null=True)),
                ("start_time", models.TimeField()),
                ("end_time", models.TimeField()),
                (
                    "is_break",
                    models.BooleanField(
                        default=False, help_text="Whether this is a break, lunch, etc."
                    ),
                ),
                (
                    "session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="conference.session",
                    ),
                ),
                (
                    "speakers",
                    models.ManyToManyField(
                        blank=True,
                        related_name="schedule_items",
                        to="conference.speaker",
                    ),
                ),
            ],
            options={
                "ordering": ["session__date", "start_time"],
            },
        ),
    ]
