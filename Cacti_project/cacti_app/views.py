from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.models import User
from models import UserHelper
from models import ScheduleBlock, Day
from forms import RegistrationForm, LoginForm, SearchForm, PictureForm
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from forms import ScheduleBlockForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from json import loads
from friendship.models import Friend
from schedule import associate_user_schedule
import re
from django.core.urlresolvers import reverse


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
    # TODO: Perform the login and redirect the page to a specific url.
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
            authenticated_user = authenticate(username=username, password=password)
            authenticate(username=username, password=password)  # authentication is the logged in check?
            login(request, authenticated_user)
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
    found = False
    user = User.objects.get(username=request.user.username)

    search_query = request.GET.get('search-form')
    # breaks the input into two scenarios to check 1) by email 2) by username
    if search_query:
        # if request.method == 'GET':
        #     search_query = request.GET.get('search-form') #(key,None) key = grabs the value in 'search-form'
        #     emailRegex = r'@.*/..*'
        emailRegex = r'@'
        emailResult = re.search(emailRegex, search_query)

        # search for user by email
        if emailResult:
            try:
                friend = User.objects.get(email=search_query)
                found = True
                return search_page(request, user, friend, found)

            except ObjectDoesNotExist:
                # make block say not found search_not_found
                # return render(request,'home_page.html',context_dict)
                return search_page(request, user, user, found)
                # return HttpResponse('cant find ur friend from email')

        # search for user by username
        else:
            try:
                friend = User.objects.get(username=search_query)
                found = True
                return search_page(request, user, friend, found)
            except ObjectDoesNotExist:
                return search_page(request, user , user, found)
    else:
        return render(request, 'home_page.html', context_dict)


def search_page(request, user_instance, friend_instance, found):
    """
    results of user search for a friend, if send request button is used, friend request is sent
    :param request:
    :param user_instance: user
    :param friend_instance: friend? idk how to use these
    :return: search-page.html
    """
    context_dict = {
        'page_title': 'Cacti: Search for friends',
        'username': user_instance.username,
        'friend_username': friend_instance.username,
        'friend_email': friend_instance.email,
        'send_friend_request': '/cactiapp/send_friend_request',
        'found': found
    }
    if request.method == 'POST':
        print ('request sent to', friend_instance.username)
        Friend.objects.add_friend(request.user, friend_instance)
        return request_friend(request, user_instance, friend_instance)


def request_friend(request, user_instance, friend_instance):
    # Just renders the sent friend request page
    context_dict = {
        'page_title': 'Request sent!',
        'username': user_instance.username,
        'friend_username': friend_instance.username
    }
    # latestRequest = len(Friend.objects.sent_requests(request.user))-1
    # print ('sent requests:',Friend.objects.sent_requests(user=request.user))
    # print ('the request that you sent', Friend.objects.sent_requests(request.user)[latestRequest])
    return render(request, 'frequest_sent.html', context_dict)


def view_friends(request):
    # displays all friends and pending friend requests
    # TODO: do something about the modal ids?

    friend_requests = []
    friends = []

    context_dict = {
        'page_title': 'Cacti: Friends',
        'username': request.user.username,
        'friend_requests': friend_requests,
        'friends_list': friends
    }
    for friend_request in Friend.objects.unread_requests(request.user):
        # cleans out the string from django-friendship Ex: "User #15 sent a request to #1"
        request_sentence = str(friend_request)
        sentence_parts = request_sentence.replace('#', '').split(' ')
        requester_id = int(sentence_parts[1])
        requester = User.objects.get(id=requester_id)
        friend_requests.append(requester)
        request.name = requester.username

    for user in Friend.objects.friends(request.user):
        friends.append(user)

    if request.method == 'POST':
        if request.POST.get('accept'):
            friend_name = request.POST.get('accept', '')  # gets the value associated with the "accept" from POST request
            friend = User.objects.get(username=friend_name)
            new_relationship = Friend.objects.add_friend(request.user, friend)
            new_relationship.accept()
            # return HttpResponseRedirect(reverse_lazy('friends_page.html'))
            # return render(request, 'friends_page.html', context_dict)
            return HttpResponseRedirect('friends')

        elif request.POST.get('deny'):
            # there's no reject function with django-friendship. So accept and then unfriend :p
            not_friend_name = request.POST.get('deny', '')
            not_friend = User.objects.get(username=not_friend_name)
            temp_relationship = Friend.objects.add_friend(request.user, not_friend)
            temp_relationship.accept()
            Friend.objects.remove_friend(request.user, not_friend)
            # return HttpResponseRedirect(reverse_lazy('view_friends'))
            return HttpResponseRedirect('friends')
            # return render(request, 'friends_page.html', context_dict)

        elif request.POST.get('delete_friend'):
            df = request.POST.get('delete_friend', '')
            friend_to_delete = User.objects.get(username=df)
            Friend.objects.remove_friend(friend_to_delete, request.user)
            return HttpResponseRedirect('friends')
           # return HttpResponseRedirect(reverse_lazy('view_friends'))
            # return render(request, 'friends_page.html', context_dict)

    return render(request, 'friends_page.html', context_dict)


def view_profile(request):
    # TODO pfp file form
    u = User.objects.get(username=request.user)
    pfp_form= PictureForm(request.POST, request.FILES)
    u_helper = UserHelper.objects.get(user=u)
    u_pfp = u_helper.picture
    context_dict = {
        'page_title': 'User:Profile',
        'user_pfp': u_pfp,
        'username': request.user.username,
        'user_email': request.user.email,
        'form': pfp_form
    }
    if request.method == 'POST':
        if pfp_form.is_valid():
            u = User.objects.get(username=request.user.username)
            u_pfp = u.picture(docfile=request.FILES['picture'])
            u_pfp.save()
            return HttpResponseRedirect('profile')
        else:
            pfp_form = PictureForm() #returns empty form?

    return render(request, 'profile.html', context_dict)


# def upload_pic(request):
#     if request.method == 'POST':
#         form = PictureForm(request.POST, request.FILES)
#         if form.is_valid():
#             idk = request.user
#             user_helper = UserHelper.user(request.user)
#             # cacti_user = User.objects.get(request.user)
#             # cacti_user.
#             # m.model_pic = form.cleaned_data['image']
#             # m.save()
#             return HttpResponse('image upload success')


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
            'process_url': '/cacti_app/process-schedule',
        }
        return render(request, 'register_schedule.html', context_dict)
    else:
        context_dict = {
            'slogan': 'Looks like something went wrong...please login to use this service.',
            'redirect_url': '/cacti_app/login'
        }
        return render(request, 'redirect_page.html', context_dict)


def process_schedule_info(request):
    """
    Checks the request information, extracts the forms' data, and injects
    the information into the SQL Database via ORM.
    :param request: request Object
    :return: None
    """
    list_of_schedules = loads(request.POST['json_data'])
    associate_user_schedule(list_of_schedules, request.user)
    # Redirect the user back to the homepage
    return HttpResponseRedirect(reverse('home'))


def logout_user(request):
    logout(request)
    return render(request, 'login-page.html')
