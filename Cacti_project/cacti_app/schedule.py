from models import ScheduleBlock, Day
# TODO: Rename the string_converter python script.
from string_converter import convert_to_datetime


def associate_user_schedule(list_of_schedules, user):
    """
    Creates all of the day and schedule models in the database, if the
    models don't exist already and associates all the Day, ScheduleBlock, and Users
    together.
    :param list_of_schedules: list
    :param user: User object
    :return: None
    """
    schedule_list = list_of_schedules
    for schedule in schedule_list:
        # Create all of the days if the models don't exist in the DB
        get_or_create_days()
        # Create the schedule_object in the database
        # TODO: Assign the ScheduleBlock the day and user model.
        schedule_object, is_created = ScheduleBlock.objects.get_or_create(
            schedule_name=schedule['schedule_name'],
            start_time=convert_to_datetime(schedule['start_time']),
            end_time=convert_to_datetime(schedule_list['end_time']),
            schedule_desc=schedule['schedule_description'],
            user=user,
        )

        # Save the ScheduleBlock
        schedule_object.save()

        for day_name in schedule['weekdays']:
            # TODO: Get the day object
            day_object = Day.objects.get(day=day_name)
            # TODO: Add the user to the Day object
            day_object.user.add(user)
            # TODO: Add the Day object to the ScheduleBlock
            schedule_object.day.add(day_object)
            # TODO: Save the objects.
            day_object.save()
            schedule_object.save()


def get_or_create_days():
    """
    Wrapper function around Django's get_or_create function.
    :return: None
    """
    list_of_days = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday'
    ]
    for day in list_of_days:
        # Create the Day models and save them.
        Day.objects.get_or_create(day=day).save()
