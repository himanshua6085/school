# Generated by Django 3.0.2 on 2020-01-26 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
        ('subject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='classroom',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='classroom.Classroom'),
            preserve_default=False,
        ),
    ]
