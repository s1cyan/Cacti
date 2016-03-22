from django.conf.urls import url

from . import views

urlpatterns = [
    # TODO: Add urls
    url(r'^$', views.greeting_page, name='greeting_page'),
    url(r'^login', views.login_page, name='login'),
    url(r'^register', views.register_page, name='register'),
    url(r'^registration_processing', views.registration_processing, name= 'processing'),
    url(r'^thankyou', views.thank_you, name='thankyou'),

]
