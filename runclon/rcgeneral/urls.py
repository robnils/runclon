from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^$', views.index),
    url(r'^register', views.register, name='register'),
    url(r'^get_registrations', views.get_registrations, name='get_registrations'),
]
