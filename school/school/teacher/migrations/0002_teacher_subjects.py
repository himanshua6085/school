# Generated by Django 3.0.2 on 2020-01-26 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0003_remove_subject_teacher'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='subjects',
            field=models.ManyToManyField(to='subject.Subject'),
        ),
    ]
