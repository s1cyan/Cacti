from django.conf.urls import url
from . import views
from . import hidden_views


urlpatterns = [
    # TODO: Add urls
    url(r'^$', views.greeting_page, name='greeting_page'),
    url(r'^login', views.login_page, name='login'),
    url(r'^register', views.register_page, name='register'),
    url(r'^set-your-schedule', views.register_schedule_information,
        name='set-your-schedule'),
    url(r'^process-schedule', views.process_schedule_info, name='process_schedule'),
    url(r'^registration_processing',
        views.registration_processing, name='processing'),
    url(r'^thankyou', views.thank_you, name='thankyou'),
    url(r'home', views.home, name='home'),
    url(r'search', views.search_page, name='search'),
    url(r'send_friend_request',views.request_friend,name='send_friend_request'),
    url(r'friends', views.view_friends, name='friends'),
    url(r'profile',views.view_profile, name='profile'),
    url(r'^error', hidden_views.error_message, name='error'),
]

