# Generated by Django 4.2.7 on 2024-11-18 07:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quiz", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="questions",
            name="ques_category",
            field=models.CharField(
                choices=[
                    ("Math", "Math"),
                    ("Science", "Science"),
                    ("History", "History"),
                    ("Geography", "Geography"),
                    ("Technology", "Technology"),
                ],
                default="Math",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="questions",
            name="ques_difficulty",
            field=models.CharField(
                choices=[("Easy", "Easy"), ("Medium", "Medium"), ("Hard", "Hard")],
                default="Medium",
                max_length=10,
            ),
        ),
    ]
