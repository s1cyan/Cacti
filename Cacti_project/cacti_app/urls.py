from django.conf.urls import url

from . import views

urlpatterns = [
    # TODO: Add urls
    url(r'^$', views.greeting_page, name='greeting_page'),
    url(r'^login', views.login_page, name='login'),
    url(r'^register', views.register_page, name='register'),
    url(r'^login', views.login, name='login'),
    url(r'^set-your-schedule', views.post_registration, name='post-Registration'),
    url(r'^profile', views.profile, name='profile'),
    # url(r'^registration', views.registration, name='registration'),
    url(r'^search', views.search, name='search'),

]
