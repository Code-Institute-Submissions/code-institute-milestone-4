# Generated by Django 3.0.4 on 2020-05-11 20:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0055_auto_20200510_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 11, 20, 33, 13, 767126, tzinfo=utc)),
        ),
    ]
