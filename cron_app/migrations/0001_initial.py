# Generated by Django 4.2.7 on 2023-11-05 14:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CronExecutionLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('success', models.BooleanField(default=False)),
                ('task_name', models.CharField(max_length=255)),
                ('execution_time', models.DateTimeField(default=datetime.datetime(2023, 11, 5, 20, 16, 19, 69046))),
            ],
        ),
    ]