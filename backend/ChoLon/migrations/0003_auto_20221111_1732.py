# Generated by Django 2.1.4 on 2022-11-11 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChoLon', '0002_alter_usermodel_email_alter_usermodel_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
