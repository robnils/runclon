from django.conf.urls import url

from . import views

urlpatterns = [
    # Pages
    url(r'^index', views.index_page, name='index'),
    url(r'^$', views.index_page),
    url(r'^$rcgeneral', views.index_page),
    url(r'^search_page', views.search_page, name='search_page'),

    # Views
    url(r'^add', views.add, name='add'),
    url(r'^get_registrations', views.get_registrations, name='get_registrations'),
    url(r'^clear_all', views.clear_all, name='clear_all'),
    url(r'^register', views.register, name='register'),
    url(r'^search_by_last_name', views.search_last_name, name='search_last_name'),
    url(r'^search_by_first_name', views.search_by_first_name, name='search_first_name'),
    url(r'^fetch_statistics', views.fetch_statistics, name='fetch_statistics'),
]
