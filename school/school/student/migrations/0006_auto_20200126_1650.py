# Generated by Django 3.0.2 on 2020-01-26 11:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20200126_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relative',
            name='number',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(7000000000), django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]
