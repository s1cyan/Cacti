from django.conf.urls import url

from . import views

urlpatterns = [
    # TODO: Add urls
    url(r'^$', views.greetings, name='greetings'),
    url(r'^friends', views.friends, name='friends'),
    url(r'^home', views.home, name='home'),
    url(r'^login', views.login, name='login'),
    url(r'^set-your-schedule', views.post_registration, name='post-Registration'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^registration', views.registration, name='registration'),
    url(r'^search', views.search, name='search'),

]