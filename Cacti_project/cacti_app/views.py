from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def greetings(request):
    context_dict = {
            'page_title': 'Cacti'
            }
    return render(request, 'greetings.html', context_dict)


def friends(request):
    context_dict = {'page_title': 'Cacti: Friends'}
    return render(request,'friends_page.html',context_dict)


def home(request):
    context_dict = {'page_title': 'Cacti: Home'}
    return render(request, 'home-page.html',context_dict)


def login(request):
    context_dict = {'page_title': 'Cacti: Login'}
    return render(request, 'login-page.html',context_dict)


def post_registration(request):
    context_dict = {'page_title': 'Setting up your schedule'}
    return render(request, 'post-registration.html',context_dict)


def profile(request):
    context_dict = {'page_title': 'Cacti:Profile'}
    return render(request, 'post-registration.html',context_dict)


def registration(request):
    context_dict = {'page_title': 'Register for Cacti'}
    return render(request, 'registration.html',context_dict)


def search(request):
    context_dict = {'page_title': 'Cacti: Search for friends'}
    return render(request, 'search-page.html',context_dict)