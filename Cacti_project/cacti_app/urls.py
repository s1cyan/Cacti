from django.conf.urls import url
from . import views

urlpatterns = [
    # TODO: Add urls
    url(r'^$', views.greeting_page, name='greeting_page'),
    url(r'^login', views.login_page, name='login'),
    url(r'^register', views.register_page, name='register'),
    url(r'^set-your-schedule', views.register_schedule_information,
        name='set-your-schedule'),
    url(r'^process-schedule', views.process_sched_info,
        name='process-schedule')
]
