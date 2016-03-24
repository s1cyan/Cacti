from models import ScheduleBlock, Day


def create_day_model(days_list, schedule_model):
    """
    Associates the days inputted in from post-registration.html for the 'Days'
    field wih an integer compliant to datetime.isonweekday().
    :param days_list: list, list of days
    :param schedule_model: ScheduleBlock
    """
    print days_list
    day_dict = {
        'Monday': 1,
        'Tuesday': 2,
        'Wednesday': 3,
        'Thursday': 4,
        'Friday': 5,
        'Saturday': 6,
        'Sunday': 7
    }
    for day in days_list:
        pass
        # day_obj = Day.objects.create(date=str(day_dict[day]),
        #                              schedule_block=schedule_model)
