# Generated by Django 3.0.4 on 2020-04-14 09:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200414_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 14, 9, 31, 33, 602519, tzinfo=utc)),
        ),
    ]
