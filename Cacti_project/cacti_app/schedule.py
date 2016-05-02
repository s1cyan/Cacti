from models import ScheduleBlock, Day
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
        # TODO: Query the Day model from the database.
        # Create the schedule_object in the database
        schedule_object, is_create = ScheduleBlock.objects.get_or_create(
            schedule_name=schedule['schedule_name'],
            start_time=convert_to_datetime(schedule['start_time']),
            end_time=convert_to_datetime(schedule_list['start_time']),
            schedule_desc=schedule['schedule_description'],
            user=user
        )

    pass


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
        Day.objects.get_or_create(day=day)
