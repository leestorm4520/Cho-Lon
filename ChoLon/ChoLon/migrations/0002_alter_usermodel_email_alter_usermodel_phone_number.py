# Generated by Django 4.1.3 on 2022-11-08 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ChoLon", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usermodel",
            name="email",
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name="usermodel",
            name="phone_number",
            field=models.CharField(max_length=15),
        ),
    ]
