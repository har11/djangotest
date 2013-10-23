from django.conf.urls import patterns, url
from approba import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^machinelist', login_required(views.machinelist.as_view(),login_url='/approba/login'), name='machinelist'),
    url(r'^newmachine', views.newmachine, name='newmachine'),
    url(r'^(?P<machine_id>\d+)/editmachine/$', views.editmachine, name='editmachine'),
    url(r'^(?P<machine_id>\d+)/deletemachine/$', views.deletemachine, name='deletemachine'),
    
    url(r'^agrofieldlist', login_required(views.agrofieldlist.as_view(),login_url='/approba/login'), name='agrofieldlist'),
    url(r'^newagrofield', views.newagrofield, name='newagrofield'),
    url(r'^(?P<agrofield_id>\d+)/editagrofield/$', views.editagrofield, name='editagrofield'),
    url(r'^(?P<agrofield_id>\d+)/deleteagrofield/$', views.deleteagrofield, name='deleteagrofield'),
    
	 url(r'^fieldoperations', login_required(views.fieldoperationlist.as_view(),login_url='/approba/login'), name='fieldoperations'),
	 url(r'^newfieldoperation', views.new_fieldoperation, name='new_fieldoperation'),
    url(r'^(?P<fieldoperation_id>\d+)/editfieldoperation/$', views.editfieldoperation, name='editfieldoperation'),
    url(r'^(?P<fieldoperation_id>\d+)/deletefieldoperation/$', views.deletefieldoperation, name='deletefieldoperation'),

    url(r'^login/$', 'django.contrib.auth.views.login',name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^userprofile/$', views.userprofile, name='userprofile'),
    #It works with password change done only, but it has to be defined in the root's (project) url.py
    url(r'^userprofile/password_change/$', "django.contrib.auth.views.password_change", name='password_change'),
    url(r'^userprofile/inactivation/$', views.user_inactivate, name='user_inactivate'),
 )