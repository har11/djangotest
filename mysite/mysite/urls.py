from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	 url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^misiproba/', include('misiproba.urls', namespace="misiproba")),
    url(r'^approba/', include('approba.urls', namespace="approba")),
    
    #For making the password change work
    url(r'^password_change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    
    #Password reset, all of the built in django solution have to be used in the project's default directory
    #Cool doc is here: http://drumcoder.co.uk/blog/2010/apr/09/django-reset-password/
    (r'^accounts/password/reset/$', 'django.contrib.auth.views.password_reset', 
        {'post_reset_redirect' : '/accounts/password/reset/done/'}),
	 (r'^accounts/password/reset/done/$', 'django.contrib.auth.views.password_reset_done'),
	 (r'^accounts/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', 
        {'post_reset_redirect' : '/accounts/password/done/'}),
	 (r'^accounts/password/done/$', 'django.contrib.auth.views.password_reset_complete'),
)
