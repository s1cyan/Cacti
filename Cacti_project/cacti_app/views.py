from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from models import ScheduleBlock, Day
from forms import RegistrationForm, LoginForm, SearchForm
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from forms import ScheduleBlockForm
from django.http import HttpResponseRedirect, HttpResponse
from json import loads
from string_converter import convert_to_datetime
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
        'home_page': '/cacti_app/home',
    }
    if request.method == 'POST':
        password = request.POST['password']
        username = request.POST['username']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('home')
        else:
            print('id/password is incorrect')
            return render(request, 'login_page.html', context_dict)

    else:
        return render(request, 'login_page.html', context_dict)


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
        'ty_url': '/cactu_app/thankyou',
        'process_registration': '/cacti_app/registration_processing'
    }
    return render(request, 'registration.html', context_dict)


def registration_processing(request):
    """
    First checks if password and confirmation password are the same
    checks if email/username for registration is already in database
    :param request:
    :return: if password confirmation is incorrect and if username/email is already used : registration.html
            else: ty_page.html
    """
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    confirmation = request.POST['confirm']

    if password != confirmation:
        print ('passwords not the same')
        return register_page(request)
        # return render(request, 'registration.html')

    # have to check if email is taken- if not check if username is taken. If you do both at the same time, one not exist will register user
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
            authenticate(username=username, password=password)  # authentication is the logged in check?
            return HttpResponseRedirect('thankyou')


def thank_you(request):
    context_dict = {
        'page_title': 'Thanks!',
        # 'continue_url_INVIEWS': '/cacti_app/home'
    }
    return render(request, 'ty_page.html', context_dict)


def home(request):
    """
    :param request
    :return:
    """
    search_form = SearchForm(request.GET)
    context_dict = {
        'page_title': 'Home',
        'username': request.user.username,
        'form': search_form,
    }
    # search functionality
    user = User.objects.get(username=request.user.username)
    print ('user', user.email)
    search_query = request.GET.get('search-form')
    if search_query:
        # if request.method == 'GET':
        #     search_query = request.GET.get('search-form') #(key,None) key = grabs the value in 'search-form'
        #     emailRegex = r'@.*/..*'
        print(search_query)
        emailRegex = r'@'
        emailResult = re.search(emailRegex, search_query)
        if emailResult:
            try:
                friend = User.objects.get(email=search_query)
                return search_page(request, user, friend)

            except ObjectDoesNotExist:
                # make block say not found search_not_found
                # return render(request,'home_page.html',context_dict)
                return HttpResponse('cant find ur friend from email')

        else:
            try:
                friend = User.objects.get(username=search_query)
                return search_page(request, user, friend)


            except ObjectDoesNotExist:
                # make block say not found
                return HttpResponse('cant find ur friend from username')
    else:
        return render(request, 'home_page.html', context_dict)


def search_page(request, user_instance, friend_instance):
    context_dict = {
        'page_title': 'Cacti: Search for friends',
        'username': user_instance.username,
        'friend_username': friend_instance.username,
        'friend_email': friend_instance.email,
    }
    print('Aftersearch:', user_instance.username)
    print(friend_instance.username)
    return render(request, 'search_page.html', context_dict)


def register_schedule_information(request):
    """
    Renders the form allowing users to register their schedule information.
    This function is mapped with process_schedule_info(request).
    :param request: None
    :return: register_schedule.html
    """
    if request.user.is_authenticated():
        context_dict = {
            'page_title': 'Update your schedule',
            'schedule_url': '/cacti_app/set-your-schedule',
            'schedule_process': '/cacti_app/process-schedule',
        }
        return render(request, 'register_schedule.html', context_dict)
    else:
        # TODO: Return a page with a link to the login/register page.
        context_dict = {

        }
        return None


def process_schedule_info(request):
    """
    Checks the request information, extracts the forms' data, and injects
    the information into the SQL Database via ORM.
    :param request: request Object
    :return: None
    """
    if request.user.is_authenticated():
        list_of_schedules = loads(request['json_data'])
    else:
        return None
