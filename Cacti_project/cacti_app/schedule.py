from models import ScheduleBlock, Day


def create_day_model(days_list, schedule_model):
    """
    Associates the days inputted in from post-registration.html for the 'Days'
    field wih an integer compliant to datetime.isonweekday().
    :param days_list: list, list of days
    :param schedule_model: ScheduleBlock
    """
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
        day_obj = Day.objects.create(date=str(day_dict[day]),
                                     schedule_block=schedule_model)


def process_sched_info(querydict):
    """
    Processes the query dictionary and attempts to create the models needed
    in the database.
    :param querydict: dict
    :return: dict
    """
    # TODO: Check if the start time is less than the end time.
    # TODO: Do logic processing, if the form is correct return the user to the
    # right page, if not, spit out error
    # TODO: Delete from the database.
    post_dict = querydict.POST
    # Convert the string into actual datetime objects.
    start_time = datetime.strptime(post_dict['start_time'], '%H:%M').time()
    end_time = datetime.strptime(post_dict['end_time'], '%H:%M').time()

    if start_time < end_time:
        try:
            # If there is already an existing schedule block taking up
            # that timeframe, return the User back to the original page.
            sched_obj = ScheduleBlock.objects.get(
                schedule_name=post_dict['sched_name'],
                schedule_description=post_dict['sched_desc'],
                start_time=start_time,
                end_time=end_time
                )
            # TODO: Return the dictionary with the errors.
            return render(request, 'post-registration.html', {})
        except:
            sched_obj = ScheduleBlock.objects.create(schedule_name=post_dict['sched_name'],
                                                    schedule_desc=post_dict['sched_desc'],
                                                    start_time=start_time,
                                                    end_time=end_time
                                                    )
            create_day_model(post_dict.getlist('days'), sched_obj)
            # TODO: Return the user to the page.
    else:
        return register_schedule_information(request)
