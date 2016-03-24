from django.shortcuts import render
from forms import RegistrationForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist



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
        'processing_url_INVIEWS': '/cacti_app/registration_processing'
    }

    return render(request, 'registration.html', context_dict)


def registration_processing(request):
    if request.POST['password'] != request.POST['confirm']:
        print ('passwords not the same')
        return render(request, 'registration.html')

    # User.objects.filter(email=request.POST['password'])

    try:
        User.objects.get(email=request.POST['email'])
        print ('email exists')
        return render(request, 'registration.html')

    except ObjectDoesNotExist:
        User.objects.create(email=request.POST['email'],first_name=request.POST['username'], password=request.POST['password'])
        print ('registration worked')
        return render(request, 'ty-page.html')


    # u = User.email(request.POST['email'])
    # u, created = User.object.get_or_create(email=request.POST['email'],first_name=request.POST['username'], password=request.POST['password'])
    #
    # if created is True:
    #     print ('registration worked')
    #     return render(request, 'ty-page.html')
    #
    # else:
    #     print ('email exists')
    #     return render(request, 'registration.html')




def thank_you(request):
    context_dict = {
        'page_title': 'Thanks!'
    }
    return render(request,'ty-page.html', context_dict)


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
