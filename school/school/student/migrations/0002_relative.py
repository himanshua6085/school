# Generated by Django 3.0.2 on 2020-01-26 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('relation', models.CharField(choices=[('F', 'Father'), ('M', 'Mother'), ('G', 'Guardian'), ('O', 'Other')], max_length=1)),
            ],
        ),
    ]
