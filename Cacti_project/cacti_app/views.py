from django.shortcuts import render
from forms import RegistrationForm
from models import User


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
        'post_registration_url': '/cacti_app/post_registration_url'

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

    register_form = RegistrationForm(request.POST)
    print request.POST
    context_dict = {
        'page_title': 'Registration',
        'show_image': False,
        'form': register_form,
        'processing_url': '/cacti_app/registration_processing'
    }


    return render(request, 'registration.html', context_dict)


def registration_processing(request):
    #make case for if two passwords arent the same
    #user exists
    #user doesnt exist
    u, created = User.object.get_or_create(RegistrationForm.email,RegistrationForm.username,RegistrationForm.password)
    if created is True:
        return render(request, 'ty-page.html')

    else: return render(request, 'registration.html')



# def thank_you(request):
#     context_dict = {
#         'page_title': 'Thanks!'
#     }
#     return render(request,'ty-page.html', context_dict)


def search_page(request):
    context_dict = {'page_title': 'Cacti: Search for friends'}
    return render(request, 'search-page.html', context_dict)


def register_schedule_information(request):
    """
    Submits a post request and registers the User's schedule information
    into the database.
    
    :param request: POST
    :return: post-registration.html
    """
    return render(request, 'post-registration.html', {})
