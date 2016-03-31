from django.shortcuts import render


def error_message(request):
    """
    View holds an error message for a load request by Jquery.
    :param request: None
    :return: error_messages.html
    """
    return render(request, "error_messages.html")
