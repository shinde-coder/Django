# Generated by Django 4.1.7 on 2023-05-24 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="employee",
            old_name="emp_id",
            new_name="empid",
        ),
    ]
