# Generated by Django 4.2.7 on 2023-11-05 14:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cron_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cronexecutionlog',
            name='execution_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 5, 20, 33, 48, 956635)),
        ),
    ]
