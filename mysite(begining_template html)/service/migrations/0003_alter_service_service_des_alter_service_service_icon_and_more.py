# Generated by Django 4.1.7 on 2023-03-30 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("service", "0002_service_service_des_service_service_icon_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="service",
            name="service_des",
            field=models.TextField(default="", max_length=60),
        ),
        migrations.AlterField(
            model_name="service",
            name="service_icon",
            field=models.CharField(default="", max_length=60),
        ),
        migrations.AlterField(
            model_name="service",
            name="service_title",
            field=models.CharField(default="", max_length=50),
        ),
    ]
