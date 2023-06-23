# Generated by Django 4.1.7 on 2023-04-20 10:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employee", "0002_alter_employee_eid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="econtact",
            field=models.CharField(
                max_length=15,
                validators=[django.core.validators.RegexValidator("^\\+?1?\\d{9,15}$")],
            ),
        ),
        migrations.AlterField(
            model_name="employee",
            name="eemail",
            field=models.EmailField(
                max_length=254,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="employee",
            name="eid",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(1)]
            ),
        ),
        migrations.AlterField(
            model_name="employee",
            name="ename",
            field=models.CharField(
                max_length=100,
                validators=[django.core.validators.MinLengthValidator(1)],
            ),
        ),
    ]