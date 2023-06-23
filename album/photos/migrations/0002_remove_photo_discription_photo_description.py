# Generated by Django 4.1.7 on 2023-06-09 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("photos", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="photo",
            name="discription",
        ),
        migrations.AddField(
            model_name="photo",
            name="description",
            field=models.CharField(default=True, max_length=200),
        ),
    ]