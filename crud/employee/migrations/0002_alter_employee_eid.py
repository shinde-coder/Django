# Generated by Django 4.1.7 on 2023-04-20 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employee", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="eid",
            field=models.IntegerField(max_length=20),
        ),
    ]
