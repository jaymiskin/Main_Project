# Generated by Django 4.1.4 on 2023-01-02 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("institute_App", "0002_remove_student_master_remove_teacher_master"),
    ]

    operations = [
        migrations.CreateModel(
            name="Role",
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
                    "Role_Type",
                    models.CharField(
                        blank=True,
                        choices=[("T", "Teacher"), ("S", "Student")],
                        default="",
                        max_length=5,
                    ),
                ),
            ],
            options={
                "db_table": "role",
            },
        ),
    ]
