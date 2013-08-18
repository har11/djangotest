from django.conf.urls import patterns, url

from misiproba import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^newuser', views.newuser, name='newuser'),
    url(r'^(?P<user_id>\d+)/edituser/$', views.edituser, name='edituser'),
    url(r'^(?P<user_id>\d+)/deleteuser/$', views.deleteuser, name='deleteuser'),
    #url(r'^edituser/$', views.edituser, name='edituser')
)    
