# Generated by Django 3.0.4 on 2020-04-07 15:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200407_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 7, 15, 42, 9, 794240, tzinfo=utc)),
        ),
    ]
