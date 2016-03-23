from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ScheduleBlock(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    schedule_name = models.CharField(max_length=10)
    schedule_desc = models.CharField(max_length=64)
    user = models.ForeignKey(User)


class Day(models.Model):
    date = models.CharField(max_length=10)
    schedule_block = models.ForeignKey(ScheduleBlock)
