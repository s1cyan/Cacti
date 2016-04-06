from django.shortcuts import render

from forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User
from models import ScheduleBlock, Day
from datetime import datetime
from schedule import create_day_model
from forms import RegistrationForm,LoginForm
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from forms import DayForm, ScheduleBlockForm


def greeting_page(request):
    """
    Renders the initial page users will see, a register or login page will be
    accessible.

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
    login_form = LoginForm(request.POST)
    # TODO: Authenticate the user and log them in using Django's User model.
    context_dict = {
        'page_title': 'Login',
        'slogan': 'Let\'s get you signed up with this service.',
        'form': login_form,
        'password_check_INVIEWS': '/cacti_app/password_check'
    }
    return render(request, 'login-page.html', context_dict)


def password_check(request):
    password = request.POST['password']
    username = request.POST['username']
    p = authenticate(username=username, password=password)
    if p is not None:  # password works for user
        return render(request, 'home-page.html')
    else:
        print ('id/password incorrect')
        return render(request, 'login-page.html')


def register_page(request):
    """
    Renders the registration page and allows the user to create an account.

    :param request: POST
    :return: registration.html
    """
    register_form = RegistrationForm(request.POST)
    # print request.POST
    context_dict = {
        'page_title': 'Registration',
        'show_image': False,
        'form': register_form,
        'processing_url_INVIEWS': '/cacti_app/registration_processing'
    }
    return render(request, 'registration.html', context_dict)


def registration_processing(request):
    """
    First checks if password and confirmation password are the same
    checks if email/username for registration is already in database
    :param request:
    :return: if password confirmation is incorrect and if username/email is already used : registration.html
            else: ty-page.html
    """
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    confirmation = request.POST['confirm']

    if password != confirmation:
        print ('passwords not the same')
        return render(request, 'registration.html')

    try:
        User.objects.get(email=email)
        User.objects.get(username=username)
        print ('email/username already exists')
        return render(request, 'registration.html')

    except ObjectDoesNotExist:
        User.objects.create_user(username=username, email=email, password=password)
        authenticate(username = username, password = password) #authentication is the logged in check?
        return render(request, 'ty-page.html')


def thank_you(request):
    context_dict = {
        'page_title': 'Thanks!',
        # 'continue_url_INVIEWS': '/cacti_app/home'
    }
    return render(request, 'ty-page.html', context_dict)


def home(request):
    context_dict = {
        'page_title': 'Home',
    }
    return render(request, 'home-page.html', context_dict)


def search_page(request):
    context_dict = {'page_title': 'Cacti: Search for friends'}
    return render(request, 'search-page.html', context_dict)


def register_schedule_information(request):
    """
    Renders the form allowing users to register their schedule information.
    This function is mapped with process_sched_info(request).
    :param request: None
    :return: post-registration.html
    """
    # TODO: Check if the user is logged in.
    form = ScheduleBlockForm(request.POST)
    context_dict = {
            'page_title': 'Update your schedule',
            'schedule_url': '/cacti_app/set-your-schedule',
            'schedule_process': '/cacti_app/process-schedule',
            'form': form
            }
    return render(request, 'post-registration.html', context_dict)


def process_sched_info(request):
    """
    Processes the query dictionary and attempts to create the models needed
    in the database.
    :param request: dict
    :return: None
    """
    try:
        pass
    except:
        pass
    pass
