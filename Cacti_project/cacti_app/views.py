from django.shortcuts import render, redirect, render_to_response
from forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User
from models import ScheduleBlock, Day
from datetime import datetime
from schedule import create_day_model
from forms import RegistrationForm,LoginForm,SearchForm
from django.contrib.auth import authenticate,login,logout
from django.core.exceptions import ObjectDoesNotExist
from forms import ScheduleBlockForm
from django.http import HttpResponseRedirect, HttpResponse
from json import loads
from friendship.models import Friend
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
        'home_page':'/cacti_app/home',
    }
    if request.method == 'POST':
        password = request.POST['password']
        username = request.POST['username']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('home')
        else:
            print('id/password is incorrect')
            return render(request,'login-page.html',context_dict)

    else:
        return render(request, 'login-page.html', context_dict)


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
        # this except - is when the user gets registered
        except ObjectDoesNotExist:
            User.objects.create_user(username=username, email=email, password=password)
            authenticate(username=username, password=password) #authentication is the logged in check?
            return HttpResponseRedirect('thankyou')


def thank_you(request):
    context_dict = {
        'page_title': 'Thanks!',
        # 'continue_url_INVIEWS': '/cacti_app/home'
    }
    return render(request, 'ty-page.html', context_dict)


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
    # print ('user', user.email)
    search_query = request.GET.get('search-form')
    #breaks the input into two scenarios to check 1) by email 2) by username
    if search_query:
        # print(search_query)
        emailRegex = r'@'
        emailResult = re.search(emailRegex,search_query)
        #search for user by email
        if emailResult:
            try:
                friend = User.objects.get(email=search_query)
                return search_page(request,user,friend)

            except ObjectDoesNotExist:
                # TODO make the main block say could not find user
                # make block say not found search_not_found
                # return render(request,'home-page.html',context_dict)
                return HttpResponse('cant find ur friend from email')
        #search for user by username
        else:
            try:
                friend = User.objects.get(username=search_query)
                return search_page(request,user,friend)


            except ObjectDoesNotExist:
                # TODO make the main block say could not find user
                return HttpResponse('cant find ur friend from username')
    else:
        return render(request, 'home-page.html', context_dict)


def search_page(request,user_instance, friend_instance):
    context_dict = {
        'page_title':'Cacti: Search for friends',
        'username': user_instance.username,
        'friend_username': friend_instance.username,
        'friend_email': friend_instance.email,
        'send_friend_request':'/cactiapp/send_friend_request'
    }
    print friend_instance.email
    if request.method == 'POST':
        # users_friend = User.objects.get(friend_instance)
        print ('request sent to', friend_instance.username)
        Friend.objects.add_friend(request.user, friend_instance)
        return friend_request(request,user_instance,friend_instance)
        # return HttpResponseRedirect('send_friend_request')
    #     # print (Friend.objects.friends(request.user))
    #     # return HttpResponse('request sent?')
    #     # return render_to_response('frequest_sent.html',context_instance=RequestContext(request))
    #     # return HttpResponseRedirect('friended')
    #     return friend_request(request,user_instance,friend_instance)
    return render(request, 'search-page.html', context_dict)


def friend_request(request, user_instance, friend_instance):
    context_dict = {
        'page_title': 'Request sent!',
        'username': user_instance.username,
        'friend_username': friend_instance.username
        # 'friend_username': friend_instance.username,
    }
    latestRequest = len(Friend.objects.sent_requests(request.user))-1
    print ('sent requests:',Friend.objects.sent_requests(user=request.user))
    print ('friends list',Friend.objects.friends(request.user))
    print ('the request that you sent', Friend.objects.sent_requests((request.user))[latestRequest])
    # return HttpResponse('request sent?')
    return render(request,'frequest_sent.html', context_dict)
#
# def friend_request(request, user_instance, friend_instance):
#     # TODO use friendship package to send friend link.
#     context_dict = {
#         'page_title': 'Cacti',
#         'username': user_instance.username,
#         'friend_username': friend_instance.username,
#     }
#     Friend.objects.add_friend(request.user_instance, friend_instance)
#     print (Friend.objects.friends(request.user_instance))
#     return render(request,'frequest_sent.html', context_dict)


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
    # print (request.user.is_authenticated())
    # print request.user
    return render(request, 'post-registration.html', context_dict)


def process_schedule_info(request):
    """
    Processes the query dictionary and attempts to create the models needed
    in the database.
    :param request: dict
    :return: None
    """
    print request.POST
    # TODO: Load the json object as a python readable dictionary.
    json_post = loads(request.POST['json_data'])
    print json_post


def logout_user(request):
    logout(request)
    return render(request,'login-page.html')
