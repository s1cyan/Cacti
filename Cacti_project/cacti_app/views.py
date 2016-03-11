from django.shortcuts import render
from django.http import HttpResponse


def greeting_page(request):
    """
        Renders the initial page users will see.

        :param request: None
        :return: greetings.html
    """
    context_dict = {
            'page_title': 'Cacti',
            'slogan': 'We need a slogan.',
            'login_url': 'some_url',
            'register_url': 'another_url'
            }
    return render(request, 'greetings.html', context_dict)


def login_page(request):
    # TODO: Check for GET request and check the database.
    # TODO: Return the render template and route this function to a url.
    pass


def register_page(request):
    # TODO: Check for POST request and add the user to the database.
    # TODO: Return the render tempalte and route this function to a url.
    # TODO: Check if the Username and Email address exists.
    pass
