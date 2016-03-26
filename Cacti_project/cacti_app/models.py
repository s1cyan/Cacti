from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User


# Create your models here.

# class User(models.Model):
#     username = models.CharField(max_length=64)
#     email = models.EmailField()
#     phone_number = models.IntegerField(max_length=11)
#     password = models.CharField(max_length=64)
#     status = models.BooleanField()
#     friends = models.ManyToManyField("self")
#     picture = models.ImageField()

# class UserHelper(models.Model):
#     friends = models.ManyToManyField("self")
#     picture = models.ImageField()
#     status = models.BooleanField()
#     phone_number = models.IntegerField(max_length=11)
#     user = models.OneToOneField(User)


class ScheduleBlock(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.CharField(max_length=64)
    user = models.ForeignKey(User)


class Day(models.Model):
    date = models.CharField(max_length=10)
    block = models.ForeignKey(ScheduleBlock)