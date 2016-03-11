from django.conf.urls import url

from . import views

urlpatterns = [
    # TODO: Add urls
    url(r'^$', views.greeting_page, name='greeting_page'),
    url(r'^cacti_app/login', views.login_page, name='login'),
    url(r'^cacti_app/register', views.register_page, name='register'),
]
