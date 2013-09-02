from django.conf.urls import patterns, url

from approba import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^machinelist', views.machinelist.as_view(), name='machinelist'),
    url(r'^newmachine', views.newmachine, name='newmachine'),
    url(r'^(?P<machine_id>\d+)/editmachine/$', views.editmachine, name='editmachine'),
    url(r'^(?P<machine_id>\d+)/deletemachine/$', views.deletemachine, name='deletemachine'),
    url(r'^login/$', 'django.contrib.auth.views.login',name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    )