# Generated by Django 3.0.2 on 2020-01-26 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_relative'),
    ]

    operations = [
        migrations.AddField(
            model_name='relative',
            name='student',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
            preserve_default=False,
        ),
    ]