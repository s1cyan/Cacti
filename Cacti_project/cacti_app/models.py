from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Day(models.Model):
    day = models.CharField(max_length=9)
    user = models.ManyToManyField(User)

    # Return the identifier for the Day model
    def __unicode__(self):
        return self.day
    

class UserHelper(models.Model):
    picture = models.ImageField()
    status = models.BooleanField()
    user = models.OneToOneField(User)


class ScheduleBlock(models.Model):
    schedule_name = models.CharField(max_length=10, primary_key=True)
    schedule_desc = models.CharField(max_length=128)
    start_time = models.TimeField()
    end_time = models.TimeField()
    day = models.ManyToManyField(Day)
    user = models.OneToOneField(User)

    # Return the identifier for the ScheduleBlock
    def __unicode__(self):
        return self.schedule_name
