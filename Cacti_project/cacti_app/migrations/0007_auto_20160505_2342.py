# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-05 23:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cacti_app', '0006_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userhelper',
            name='friends',
        ),
        migrations.RemoveField(
            model_name='userhelper',
            name='phone_number',
        ),
    ]