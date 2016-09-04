from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^$', views.index),
    url(r'^add', views.add, name='add'),
    url(r'^get_registrations', views.get_registrations, name='get_registrations'),
    url(r'^clear_all', views.clear_all, name='clear_all'),
    url(r'^register', views.register, name='register'),
]
