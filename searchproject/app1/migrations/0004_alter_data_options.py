# Generated by Django 4.2.2 on 2023-06-13 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0003_alter_data_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="data",
            options={"verbose_name": "Data1", "verbose_name_plural": "Data1"},
        ),
    ]
