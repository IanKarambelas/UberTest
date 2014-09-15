#boilerplate code
from django.conf.urls import patterns, url

from emailapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)