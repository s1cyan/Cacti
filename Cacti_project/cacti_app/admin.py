from django.contrib import admin
from models import Day, User, ScheduleBlock

# Register your models here.
admin.site.register(User)
admin.site.register(Day)
admin.site.register(ScheduleBlock)

