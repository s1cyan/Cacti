# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-26 23:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cacti_app', '0006_auto_20160326_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduleblock',
            name='end_time',
            field=models.TimeField(verbose_name=datetime.datetime(2016, 3, 26, 23, 16, 57, 606102, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='scheduleblock',
            name='start_time',
            field=models.TimeField(verbose_name=datetime.datetime(2016, 3, 26, 23, 16, 57, 606061, tzinfo=utc)),
        ),
    ]
