from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class ScheduleBlock(models.Model):
    schedule_name = models.CharField(max_length=10, primary_key=True)
    schedule_desc = models.CharField(max_length=128)
    start_time = models.TimeField(timezone.now())
    end_time = models.TimeField(timezone.now())
    user = models.ForeignKey(User)


class Day(models.Model):
    date = models.IntegerField()
    schedule_block = models.ForeignKey(ScheduleBlock)
