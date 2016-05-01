from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Day(models.Model):
    day = models.IntegerField()
    user = models.ForeignKey(User)
    

class UserHelper(models.Model):
    friends = models.ManyToManyField("self")
    picture = models.ImageField(upload_to='profile_pictures/')
    status = models.BooleanField()
    phone_number = models.IntegerField(max_length=11)
    user = models.OneToOneField(User)


class ScheduleBlock(models.Model):
    schedule_name = models.CharField(max_length=10, primary_key=True)
    schedule_desc = models.CharField(max_length=128)
    start_time = models.TimeField(default=timezone.now())
    end_time = models.TimeField(default=timezone.now())
    day = models.ForeignKey(Day)
    user = models.ForeignKey(User)

    # Allows ease of debugging by returning an identifier.
    def __unicode__(self):
        return self.schedule_name
