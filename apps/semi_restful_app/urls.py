from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^shows$', views.index),
    url(r'^process_form$', views.process),
    url(r'^shows/new$', views.new_show),
    url(r'^shows/(?P<show_id>\d+)$', views.show),
    url(r'^shows/(?P<show_id>\d+)/edit$', views.edit),
    url(r'^process_edit/(?P<show_id>\d+)$', views.process_edit),
    url(r'^delete/(?P<show_id>\d+)$', views.destroy)
]
