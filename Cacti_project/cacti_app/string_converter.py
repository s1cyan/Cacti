from datetime import datetime


def convert_to_datetime(time_string):
    """
    Converts a string into a datetime object that is Python
    readable.
    :param time_string: string
    :return: datetime
    """
    time = datetime.strptime(time_string, '%H:%M').time()
    return time


def weekday_to_int(weekday_string):
    """
    Maps a weekday string to the integer value by following datetime.datetime.weekday()
    format.
    :param weekday_string: string, Name of the day
    :return:
    """

    weekday_dict = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4,
        'Saturday': 5,
        'Sunday': 6,
    }

    try:
        # If our string exists within the dictionary, return the integer associated
        # with the value.
        return weekday_dict[weekday_string]
    except LookupError as error:
        # Otherwise return nothing, because it does not exist.
        return None
