# Generated by Django 4.1.3 on 2022-11-14 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task_manager", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="deadline",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
