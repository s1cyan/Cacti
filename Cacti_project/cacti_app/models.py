from __future__ import unicode_literals

from django.db import models

# from django.contrib.auth import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    phone_number = models.IntegerField(max_length=11)
    password = models.CharField(max_length=64)
    status = models.BooleanField()
#   TODO Picture thing


class Classes(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.CharField(max_length = 64)


class Day(models.Model):
    date = models.DateField()