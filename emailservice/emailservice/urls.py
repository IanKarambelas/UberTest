#boilerplate code
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'emailservice.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^emailapp/', include('emailapp.urls')),	#this line written by me
    url(r'^admin/', include(admin.site.urls)),
)
