from django.conf.urls import url

from . import views

urlpatterns = [
    # TODO: Add urls
    url(r'^$', views.greeting_page, name='greeting_page'),
]
