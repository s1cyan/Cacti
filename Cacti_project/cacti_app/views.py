from django.shortcuts import render


def greeting_page(request):
    """
    Renders the initial page users will see.

    :param request: None
    :return: greetings.html
    """
    context_dict = {
            'page_title': 'Cacti',
            'slogan': 'We need a slogan.',
            'show_image': True,
            'register_url': '/cacti_app/register',
            'login_url': '/cacti_app/login'
            }
    return render(request, 'greetings.html', context_dict)


def login_page(request):
    """
    Renders the login page for users to sign in.

    :param request: POST
    :return: login.html
    """
    # TODO: Check for GET request and check the database.
    # TODO: Return the render template and route this function to a url.
    context_dict = {
        'page_title': 'Login',
        'slogan': 'Let\'s get you signed up with this service.',
    }
    return render(request, 'login-page.html', context_dict)


def register_page(request):
    """
    Renders the registration page and allows the user to create an account.

    :param request: POST
    :return: registration.html
    """
    # TODO: Check for POST request and add the user to the database.
    # TODO: Check if the Username and Email address exists.
    context_dict = {
        'page_title': 'Registration',
        'show_image': False
    }
    return render(request, 'registration.html', context_dict)
