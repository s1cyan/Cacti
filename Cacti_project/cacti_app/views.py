from django.shortcuts import render

from forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User
from models import ScheduleBlock, Day
from datetime import datetime
from schedule import create_day_model
from forms import RegistrationForm,LoginForm,SearchForm
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from forms import DayForm, ScheduleBlockForm
import re


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
    context_dict = {
        'page_title': 'Login',
        'slogan': 'Login to Cacti',
        'form': login_form,
        'password_check_INVIEWS': '/cacti_app/password_check'
    }

    return render(request, 'login-page.html', context_dict)


def password_check(request):
    password = request.POST['password']
    username = request.POST['username']
    p = authenticate(username=username, password=password)
    if p is not None:  # password works for user
        return home(request,p)
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
        'slogan': 'Let\'s get you signed up with this service.',
        'show_image': False,
        'form': register_form,
        'ty_url':'/cactu_app/thankyou',
        'process_registration': '/cacti_app/registration_processing'
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
        return register_page(request)
        # return render(request, 'registration.html')

#have to check if email is taken- if not check if username is taken. If you do both at the same time, one not exist will register user
    try:
        User.objects.get(email=email)
        print ('email already exists')
        return render(request, 'registration.html')

    except ObjectDoesNotExist:
        try:
            User.objects.get(username=username)
            print ('username already exists')
            return render(request, 'registration.html')
        except ObjectDoesNotExist:
            User.objects.create_user(username=username, email=email, password=password)
            authenticate(username=username, password=password) #authentication is the logged in check?
            return thank_you(request)


def thank_you(request):
    context_dict = {
        'page_title': 'Thanks!',
        # 'continue_url_INVIEWS': '/cacti_app/home'
    }
    return render(request, 'ty-page.html', context_dict)


def home(request, user_instance):
    '''
    :param user_instance: User
    :return:
    '''
    search_form = SearchForm(request.GET)
    context_dict = {
        'page_title': 'Home',
        'username': user_instance.username,
        'form': search_form,
    }
    if request.method == 'GET':
        search_input = request.GET.get('search-form') #(key,None) key = grabs the value in 'search-form'
        emailRegex = r'@.*/..*'
        emailResult = (emailRegex,input)
        if emailResult:
            try:
                user = User.objects.get(email=search_input)
                username = user.username
                email = user.email

            except ObjectDoesNotExist:
                # make block say not found search_not_found
                return render(request)
        else:
            try:
                user = User.objects.get(username=search_input)
                username = user.username
                email = user.email
            except ObjectDoesNotExist:
                # make block say not found
                return render(request)
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

#
# def search(request):
#     input = request.POST['search']
#     emailRegex = r'@.*/.com'
#     emailResult = (emailRegex,input)
#     if emailResult:
#         try:
#             User.objects.get(email = input)
#             return render(request,'search-page.html') #change the contents of the search page to have the user's info
#
#         except ObjectDoesNotExist:
#             return render(request,'search-page.html')# contents = user not found
