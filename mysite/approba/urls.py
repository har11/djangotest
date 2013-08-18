from django.conf.urls import patterns, url

from approba import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^newmachine', views.newmachine, name='newmachine'),
    url(r'^(?P<machine_id>\d+)/editmachine/$', views.editmachine, name='editmachine'),
    url(r'^(?P<machine_id>\d+)/deletemachine/$', views.deletemachine, name='deletemachine'),
    )