# Generated by Django 2.1.4 on 2022-11-11 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChoLon', '0004_auto_20221111_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='pPrice',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='pQuantity',
            field=models.CharField(max_length=5),
        ),
    ]
